from sceptre.context import SceptreContext
from sceptre.plan.plan import SceptrePlan

context = SceptreContext(
    project_path='.',
    command_path='experimental'
)

plan = SceptrePlan(context)
change_sets = plan.describe_change_set('test-change-set')
print(change_sets)