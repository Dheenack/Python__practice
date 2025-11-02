# %%
class Employee:
    company_name = "TechCorp"

    @classmethod
    def change_company_name(cls, new_name):
        print(f"[ClassMethod] Changing {cls.__name__}.company_name to '{new_name}'")
        cls.company_name = new_name

    @staticmethod
    def try_to_change_company_name(new_name):
        print(f"[StaticMethod] Changing Employee.company_name to '{new_name}'")
        Employee.company_name = new_name

    @classmethod
    def get_company_name(cls):
        return cls.company_name

# %%
class Manager(Employee):
    pass

# %%
# Example usage
if __name__ == "__main__":
    print("Initial values:")
    print("Employee:", Employee.get_company_name())
    print("Manager :", Manager.get_company_name())
    print()

    
    # Change using class method on Employee
    Employee.change_company_name("InnoTech")
    print("\nAfter Employee.change_company_name('InnoTech'):")
    print("Employee:", Employee.get_company_name())
    print("Manager :", Manager.get_company_name())
    print()

    # Change using static method on Employee
    Employee.try_to_change_company_name("GlobalTech")
    print("\nAfter Employee.try_to_change_company_name('GlobalTech'):")
    print("Employee:", Employee.get_company_name())
    print("Manager :", Manager.get_company_name())
    print()

    # Change using class method on Manager
    Manager.change_company_name("ManagerTech")
    print("\nAfter Manager.change_company_name('ManagerTech'):")
    print("Employee:", Employee.get_company_name())
    print("Manager :", Manager.get_company_name())
    print()

    # Change using static method on Manager
    Manager.try_to_change_company_name("StaticTech")
    print("\nAfter Manager.try_to_change_company_name('StaticTech'):")
    print("Employee:", Employee.get_company_name())
    print("Manager :", Manager.get_company_name())

# %%
