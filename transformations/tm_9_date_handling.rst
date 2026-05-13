.. sectionauthor:: Laiton Hedley

.. _date-handling:

=============
Date Handling
=============

Use the techniques on this page when you need to:

- Calculate someone's age from their date of birth.
- Measure the number of days between two events (e.g., start and end of a study).
- Add or subtract days from a date (e.g., scheduling a follow-up).
- Extract the year, month, or day from a date for grouping or filtering.

.. note::
   jamovi does not have a native Date data type at this time (one is planned).
   The functions below treat dates as text or integers and allow common date
   arithmetic to be performed via :ref:`computed-variables`.

Two functions form the foundation of date handling in jamovi:

- ``DATEVALUE(var)`` — converts a date string such as ``2025-01-29`` to an
  integer representing the number of days since 1 January 1970.
- ``DATE(var)`` — performs the reverse: converts such an integer into a
  formatted date string.

The typical workflow is to convert a date to an integer, perform arithmetic on
it, and then convert the result back to a date string. Both functions
optionally accept a format string for non-standard date formats.

.. list-table:: Example date formatting
   :header-rows: 1

   * - Day
     - ``DATE(Day)``
     - ``DATE(Day, "%d %m %Y")``
     - ``DATE(Day, "%m/%d/%y")``
   * - 13
     - 1970-01-13
     - 13 01 1970
     - 01/13/70
   * - 4197
     - 1981-06-29
     - 29 06 1981
     - 06/29/81

Adding Days to a Date
---------------------

Convert a date to an integer, add the number of days, then convert back:

.. list-table:: Adding 7 days to a date
   :header-rows: 1

   * - Date
     - ``DATEVALUE(Date)``
     - ``DATEVALUE(Date) + 7``
     - ``DATE(DATEVALUE(Date) + 7)``
   * - 2026-01-29
     - 20482
     - 20489
     - 2026-02-05
   * - 2024-03-10
     - 19792
     - 19799
     - 2024-03-17
   * - 2025-08-22
     - 20322
     - 20329
     - 2025-08-29

Days Elapsed Between Two Dates
------------------------------

Subtract the start date integer from the end date integer:

.. list-table:: Computing days elapsed
   :header-rows: 1

   * - StartDate
     - EndDate
     - ``DATEVALUE(EndDate) - DATEVALUE(StartDate)``
   * - 2026-01-29
     - 2026-02-15
     - 17
   * - 2024-03-10
     - 2024-04-11
     - 32
   * - 2025-08-22
     - 2024-04-11
     - -498

Extracting Year, Month, or Day
------------------------------

Use the ``SPLIT()`` function to extract parts of a date string. It splits text
by a delimiter and returns the chunk at the specified position. Note that
``SPLIT()`` returns text — wrap with ``INT()`` if you need the result as a
number for arithmetic.

.. list-table:: Extracting year, month, and day
   :header-rows: 1

   * - Date
     - ``SPLIT(Date, '-', 1)``
     - ``SPLIT(Date, '-', 2)``
     - ``SPLIT(Date, '-', 3)``
   * - 2026-01-29
     - 2026
     - 01
     - 29
   * - 2024-03-10
     - 2024
     - 03
     - 10
   * - 2025-08-22
     - 2025
     - 08
     - 22

Composing a Date from Parts
---------------------------

Concatenate year, month, and day strings with ``-`` as a separator:

.. list-table:: Composing a date from parts
   :header-rows: 1

   * - Year
     - Month
     - DayOfMonth
     - ``Year + '-' + Month + '-' + DayOfMonth``
   * - 2026
     - 01
     - 29
     - 2026-01-29
   * - 2024
     - 03
     - 10
     - 2024-03-10
   * - 2025
     - 08
     - 22
     - 2025-08-22
