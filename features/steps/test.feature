Feature: Application Login
    Scenario: User logs in with valid credentials
        Given I am on the login page
        When I enter "<EMAIL>" as username and "password" as password
        Then I should see a welcome message