from rolepermissions.roles import AbstractUserRole

class Is_employee(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
    }

class Is_staff(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }

class Admin(AbstractUserRole):
    available_permissions = {
        'drop_tables': True,
    }    