import logging

logger = logging.getLogger(__name__)


FAKE_CLAIM = """
    Part 1: Employee’s Incident Report
    Note the vague details and the "Friday Afternoon" timing.

    EMPLOYEE ACCIDENT REPORT
    Company Name: Prime Wholesale Hub
    Date of Report: Monday, November 13, 2023

    Employee Information:

    Name: Alex Rivera
    Job Title: Stock Clerk (Probationary)
    Incident Details:

    Date of Incident: Friday, November 10, 2023
    Time: "Around 4:50 PM" (10 minutes before the weekend shift ended)
    Location: Back hallway near the restrooms.
    Describe what happened: I was walking and I slipped on a mysterious wet patch. I fell hard on my back and neck. I was in too much shock to tell anyone at the time, so I just went home.
    Nature of Injury: Extreme, debilitating pain in the entire back, neck, and both shoulders. I can't move my left arm at all.
    Witnesses: None.
    Employee Signature: Alex Rivera Date: 11/13/23

    Part 2: Employer’s Internal Investigation Memo
    This is the HR manager’s private notes for the insurance company.

    TO: Mid-Atlantic Insurance Claims Dept.
    FROM: Brenda Walsh, HR Manager
    RE: Claim #88273 (Rivera, Alex)

    Observations:

    Disciplinary History: Mr. Rivera was given a final written warning for performance issues on Thursday, Nov 9—the day before the alleged injury.
    Inconsistency: When Mr. Rivera called in on Monday, he told his supervisor he "broke his back." When he arrived to fill out the form, he was observed swinging his gym bag with his left arm—the same arm he claims is now paralyzed.
    Video Footage: We reviewed footage of the hallway exit. At 5:02 PM on Friday, Mr. Rivera is seen jogging to his car in the parking lot, showing no signs of physical distress or a limp.
    Part 3: Initial Medical Report (The "Doctor Shopper")
    The employee refused the company’s clinic and went to an Emergency Room far across town.

    CITY WEST HOSPITAL – ER DISCHARGE SUMMARY
    Patient: Alex Rivera
    Chief Complaint: "10/10 pain" in back and neck.

    Clinical Notes:

    Patient arrived via private vehicle.
    Physical Exam: Patient exhibited "guarding" behavior, but when distracted during the reflex test, range of motion appeared normal.
    Diagnostic Imaging: X-rays and CT scans of the lumbar and cervical spine show no acute fractures, swelling, or abnormalities.
    Physician Note: Patient became agitated when a prescription for high-dose Oxycodone was denied. Patient specifically requested a "Total Disability" note for work for at least 6 weeks.
    Diagnosis: Soft tissue strain (unspecified).
"""

LEGIT_CLAIM = """
    Part 1: Employee’s Incident Report
    This is the first document filled out by the worker to notify the employer of the injury.

    EMPLOYEE ACCIDENT REPORT
    Company Name: Apex Logistics Solutions
    Date of Report: October 24, 2023

    Employee Information:

    Name: Jordan Smith
    Job Title: Warehouse Associate
    Department: Shipping/Receiving
    Incident Details:

    Date of Incident: October 24, 2023
    Time: 10:15 AM
    Location: Loading Dock 4
    Describe what happened: I was lifting a crate of heavy machinery parts from a pallet to a conveyor belt. As I turned to place the crate, I felt a sharp "pop" in my lower back followed by immediate pain.
    Nature of Injury: Sharp pain in lower back, radiating down the right leg.
    Witnesses: Maria Garcia (Forklift Operator)
    Employee Signature: Jordan Smith Date: 10/24/23

    Part 2: Employer’s First Report of Injury (FROI)
    The employer submits this to their insurance carrier and the state board. This is the "official" claim filing.

    STATE BOARD OF WORKERS’ COMPENSATION: FORM WC-1
    Carrier Case #: CLM-9928374-X

    EMPLOYER SECTION:

    Employer: Apex Logistics Solutions
    Address: 123 Industrial Way, Chicago, IL
    Policy Number: WC-9900221-B
    EMPLOYEE SECTION:

    Social Security No: XXX-XX-6789
    Date of Hire: 03/12/2019
    Gross Weekly Wage: $950.00
    INJURY SECTION:

    Did injury occur on premises? Yes
    Was employee performing regular duties? Yes
    Type of Injury: Lower back strain/possible disc herniation.
    Equipment involved: Manual lifting of 50lb crate.
    Initial Treatment: Sent to City Occupational Health Clinic.
    Employer Signature: Sarah Jenkins, HR Manager

    Part 3: Medical Work Status Report
    The doctor fills this out after the first exam. It tells the employer if the worker can come back to work.

    WORK STATUS REPORT
    Clinic Name: City Occupational Health
    Physician: Dr. Alan Vane

    Patient Name: Jordan Smith
    Diagnosis: Acute Lumbar Strain (ICD-10: M54.50)

    Work Status:

    [ ] May return to full duty immediately.
    [X] May return to work with the following restrictions:
    No lifting/carrying over 10 lbs.
    No prolonged standing (more than 30 minutes).
    Must be allowed to sit for 10 minutes every hour.
    [ ] Totally disabled from work until: [Date]
    Follow-up Appointment: October 31, 2023
"""

def file_content_extractor(filename: str):
    print(f"extract content from file: {filename}")

    if "fake" in filename:
        return FAKE_CLAIM

    return LEGIT_CLAIM
