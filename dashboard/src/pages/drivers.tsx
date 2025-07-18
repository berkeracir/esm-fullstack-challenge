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
} from "react-admin";

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
      <TextInput source="driver_ref" />
      <NumberInput source="number" />
      <TextInput source="code" />
      <TextInput source="forename" />
      <TextInput source="surname" />
      <DateInput source="dob" />
      <TextInput source="nationality" />
      <TextInput source="url" /> {/* TODO: URL validation */}
    </SimpleForm>
  </Create>
)

export const DriverEdit = () => (
  <Edit>
    <SimpleForm>
      <TextInput source="id" disabled />
      <TextInput source="driver_ref" />
      <NumberInput source="number" />
      <TextInput source="code" />
      <TextInput source="forename" />
      <TextInput source="surname" />
      <DateInput source="dob" />
      <TextInput source="nationality" />
      <TextInput source="url" /> {/* TODO: URL validation */}
    </SimpleForm>
  </Edit>
);
