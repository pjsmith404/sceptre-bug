from sceptre.context import SceptreContext
from sceptre.plan.plan import SceptrePlan

context = SceptreContext(
    project_path='.',
    command_path='experimental'
)

plan = SceptrePlan(context)
change_sets = plan.describe()
print(change_sets)