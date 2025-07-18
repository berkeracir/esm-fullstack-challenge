from textwrap import dedent

from esm_fullstack_challenge.config import DB_FILE
from esm_fullstack_challenge.db import DB


def get_db():
    try:
        db = DB(DB_FILE)
        yield db
    finally:
        pass


def get_next_id(table_name: str) -> int:
    # TODO: define queries as constants
    # TODO: move create_table_sql query execution to app initialization
    create_table_sql = dedent("""
        CREATE TABLE IF NOT EXISTS `id_sequence`
            (`table_name` TEXT PRIMARY KEY, `last_id` INTEGER NOT NULL DEFAULT 0)
    """).strip()
    insert_into_sql = dedent(f"""
        INSERT OR IGNORE INTO `id_sequence` (`table_name`, `last_id`)
            VALUES ("{table_name}", (SELECT IFNULL(MAX(`id`), 0) FROM `{table_name}`))
    """).strip()
    get_last_id_sql = dedent("""
        SELECT `last_id` FROM `id_sequence` WHERE `table_name` = :table_name
    """).strip()
    update_last_id_sql = dedent("""
        UPDATE `id_sequence` SET `last_id` = :new_id WHERE `table_name` = :table_name
    """).strip()

    db = next(get_db())
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute(create_table_sql)
        cur.execute(insert_into_sql)
        # TODO: make get_last_id and update_last_id queries atomic
        cur.execute(get_last_id_sql, {"table_name": table_name})
        row = cur.fetchone()

        new_id = row[0] + 1
        cur.execute(update_last_id_sql, {"new_id": new_id, "table_name": table_name})
        conn.commit()

    return new_id
