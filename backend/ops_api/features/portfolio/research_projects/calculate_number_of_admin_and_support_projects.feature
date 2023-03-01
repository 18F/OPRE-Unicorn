Feature: Calculate the number of active Administrative and Support Projects for a given Portfolio and FY.
  (Displayed on the "Projects and Spending" tab on the Portfolio details
  page in the FY XXXX Projects container.)

  Scenario: Exclude Research Projects
    Given a set of data below with the current FY 2023
      | Portfolio | Research Project | CAN | FY   | Status | Research Project Type    |
      | 1         | 1                | 1   | 2023 | active | Research Project         |
      | 1         | 2                | 1   | 2023 | active | Research Project         |
      | 1         | 3                | 2   | 2023 | active | Administrative & Support |
    When I calculate the number of active Administrative & Support Projects for a given Portfolio and FY
    Then the result should be 1.

  Scenario: Exclude Administrative & Support Projects with CANs funded exclusively from prior FY
    Given a set of data below with the current FY 2023
      | Portfolio | Research Project | CAN | FY   | Status | Research Project Type    |
      | 1         | 1                | 1   | 2022 | active | Administrative & Support |
      | 1         | 2                | 2   | 2021 | active | Administrative & Support |
    When I calculate the number of active Administrative & Support Projects for a given Portfolio and FY
    Then the result should be 0.

  Scenario: Exclude Administrative & Support Projects that are not active
    Given a set of data below with the current FY 2023
      | Portfolio | Research Project | CAN | FY   | Status   | Research Project Type    |
      | 1         | 1                | 1   | 2023 | active   | Administrative & Support |
      | 1         | 2                | 2   | 2023 | inactive | Administrative & Support |
    When I calculate the number of active Administrative & Support Projects for a given Portfolio and FY
    Then the result should be 1.
