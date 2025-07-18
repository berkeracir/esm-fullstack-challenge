import {
  Create,
  DateField,
  DateInput,
  DataTable,
  Edit,
  List,
  NumberField,
  NumberInput,
  Show,
  SimpleForm,
  SimpleShowLayout,
  TextField,
  TextInput,
  UrlField,
  required,
} from "react-admin";

const isValidHttpUrl = (value: string) => {
  let invalid = false;
  try {
    const url = new URL(value);
    if (url.protocol !== "http:" && url.protocol !== "https:") {
      invalid = true;
    }
  } catch {
    invalid = true;
  }

  if (invalid) {
    return "Invalid protocol";
  }
};
const validateUrl = [required(), isValidHttpUrl];

export const DriverList = () => (
  <List>
    <DataTable>
      <DataTable.Col source="id" />
      <DataTable.Col source="driver_ref" />
      <DataTable.Col source="number" />
      <DataTable.Col source="code" />
      <DataTable.Col source="forename" />
      <DataTable.Col source="surname" />
      <DataTable.Col source="dob">
        <DateField source="dob" />
      </DataTable.Col>
      <DataTable.Col source="nationality" />
      <DataTable.Col source="url">
        <UrlField source="url" />
      </DataTable.Col>
    </DataTable>
  </List>
);

export const DriverShow = () => (
  <Show>
    <SimpleShowLayout>
      <TextField source="id" />
      <TextField source="driver_ref" />
      <NumberField source="number" />
      <TextField source="code" />
      <TextField source="forename" />
      <TextField source="surname" />
      <DateField source="dob" />
      <TextField source="nationality" />
      <UrlField source="url" />
    </SimpleShowLayout>
  </Show>
);

export const DriverCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput source="driver_ref" validate={required()} />
      <NumberInput source="number" />
      <TextInput source="code" validate={required()} />
      <TextInput source="forename" validate={required()} />
      <TextInput source="surname" validate={required()} />
      <DateInput source="dob" validate={required()} />
      <TextInput source="nationality" validate={required()} />
      <TextInput source="url" validate={validateUrl} />
    </SimpleForm>
  </Create>
)

export const DriverEdit = () => (
  <Edit>
    <SimpleForm>
      <TextInput source="driver_ref" validate={required()} />
      <NumberInput source="number" />
      <TextInput source="code" validate={required()} />
      <TextInput source="forename" validate={required()} />
      <TextInput source="surname" validate={required()} />
      <DateInput source="dob" validate={required()} />
      <TextInput source="nationality" validate={required()} />
      <TextInput source="url" validate={validateUrl} />
    </SimpleForm>
  </Edit>
);
