# AJAX Web Form Automation

## Overview
This project focuses on automating the testing of dynamic web forms that utilize AJAX for form submission. The primary objective was to validate input handling, error scenarios, and seamless integration into a CI/CD pipeline to enhance testing efficiency and reliability.

## Tools Used
- **Selenium WebDriver** – For automating form interactions.
- **pytest** – For structuring and executing test cases.
- **Faker** – For generating realistic test data.
- **GitHub Actions** – For automating test execution in CI/CD pipelines.
- **Jenkins** – For continuous integration and deployment.

## Scope
- **Dynamic Form Interaction**: Handling AJAX-based form submissions.
- **Validation Testing**: Ensuring proper error messages for invalid inputs.
- **Data Integrity Checks**: Verifying successful submission of valid data.
- **CI/CD Integration**: Running automated tests in GitHub Actions and Jenkins.
- **Performance Optimization**: Reducing testing time by **30%** through reusable test scripts.
- **HTML Report Generation**: Creating structured reports for debugging.

## Key Achievements
- Automated form validation and submission testing.
- Improved test efficiency and coverage through **CI/CD pipeline integration**.
- Reduced testing execution time by **30%**, improving feedback cycles.
- Implemented structured **HTML reports** for easier debugging and issue tracking.

## Installation & Setup
### Prerequisites
- Python 3.x
- Selenium WebDriver
- pytest
- ChromeDriver (or appropriate WebDriver for the browser being tested)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/frankmwito/Form-submission-automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Form-submission-automation
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run tests locally:
   ```bash
   pytest -v --html=report.html
   ```

## Running Tests in CI/CD
1. Push changes to the repository.
2. GitHub Actions triggers automated test execution.
3. View results in the GitHub Actions workflow logs.

## Test Cases Overview
### Form Submission Tests
- Valid form submission
- Missing required fields validation
- Invalid email format rejection
- Duplicate data handling
- AJAX request verification

### Error Handling Tests
- Proper error messages displayed for incorrect inputs
- Server-side validation errors
- Front-end validation for instant feedback

### CI/CD Tests
- Automated test execution on push and pull requests
- Integration into Jenkins for continuous deployment
- HTML report generation for debugging

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit changes and push to GitHub.
4. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or contributions, reach out to **Franklin Muchui** via GitHub or LinkedIn.

---
This project ensures that AJAX-based web form interactions remain **efficient, reliable, and seamlessly integrated** into modern CI/CD workflows. 🚀

