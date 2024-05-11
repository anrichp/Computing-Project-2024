from behave import when, then

@when('I enter "<EMAIL>" as username and "password" as password')
def step_impl(context):
    raise NotImplementedError(
        'STEP: When I enter "<EMAIL>" as username and "password" as password'
    )


@then("I should see a welcome message")
def step_impl(context):
    raise NotImplementedError("STEP: Then I should see a welcome message")
