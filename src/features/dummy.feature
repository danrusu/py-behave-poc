Feature: Showing off behave

  Scenario: Run a simple test
    Given we set dummy preconditions
      | user | id   |
      | dan  | 1111 |
      | joe  | 2222 |

    When we do 5 dummy actions
    Then we get dummy result

  Scenario Outline: Data Driven
    Given we <message>
    Then index is <index>

    Examples:
      | message   | index |
      | behave    | 1     |
      | misbehave | 2     |
