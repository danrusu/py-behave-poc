from behave import given, when, then, step
    
@given('we set dummy preconditions')
def step_impl(context):
  for row in context.table.rows:
    print(f'{row[0]} : {row[1]}')
  pass

@when('we do {count:d} dummy actions')
def step_impl(context, count):  # -- NOTE: number is converted into integer
  assert count > 0
  context.actions_count = count
  for i in range(0, count, 1):
    print(f'dummy action {i}')

@then('we get dummy result')
def step_impl(context):  
  print(context.actions_count)
  assert context.failed is False  
  assert context.actions_count > 0

# scenario outline step
@given('we {message}')
def step_impl(context, message):  
  print(f'mssage: ${message}')
  
@then('index is {index:d}')
def step_impl(context, index):  
  print(f'index: ${index}')