.. sectionauthor:: Laiton Hedley


===================
Row and V Functions
===================

When creating formulas in jamovi, you can use either **Row functions** or
**Variable functions**. These control whether your calculation uses values from
within the same row or from an entire column.

Row Functions
-------------

Use **Row functions** when you want to calculate a value based only on other
cells in the same row. For example, if you use ``MEAN(A, B, C)``, jamovi
calculates the average of columns A, B, and C for each row individually.

.. list-table:: Example of the MEAN() function (Row-wise)
   :header-rows: 1

   * - A
     - B
     - C
     - MEAN(A, B, C)
   * - 1
     - 3
     - 4
     - 2.33
   * - 6
     - 3
     - 1
     - 3.33
   * - 5
     - 5
     - 9
     - 6.33

V Functions (Variable Functions)
--------------------------------

Use **V functions** (Variable functions) when you want to perform a calculation
using every value in a column. These are typically prefixed with the letter **V**.
For example, ``VMEAN(A)`` calculates the mean of the *entire* column A and
places that same result in every row.

.. list-table:: Example of the VMEAN() function (Variable-wise)
   :header-rows: 1

   * - A
     - B
     - C
     - VMEAN(A)
   * - 1
     - 3
     - 4
     - 4
   * - 6
     - 3
     - 1
     - 4
   * - 5
     - 5
     - 9
     - 4

You can combine Row and V functions in a single formula. A common use case is
calculating a z-score manually:

``(A - VMEAN(A)) / VSTDEV(A)``

.. note::
   For z-scores, you can also use the more concise ``Z(A)`` function.

Grouping with V Functions
-------------------------

Several V functions allow you to use a ``group_by`` parameter to calculate
values within specific categories.

Suppose you have an ``outcome`` variable and a ``Dosage`` variable (e.g.,
100 mg vs. 150 mg). To find the mean score for each dosage group separately,
use:

``VMEAN(outcome, group_by = Dosage)``

.. list-table:: Example of VMEAN() with the group_by parameter
   :header-rows: 1

   * - Dosage
     - outcome
     - VMEAN(outcome, group_by = Dosage)
   * - 150 mg
     - 4
     - 4.33
   * - 150 mg
     - 4
     - 4.33
   * - 150 mg
     - 5
     - 4.33
   * - 100 mg
     - 3
     - 3.00
   * - 100 mg
     - 2
     - 3.00
   * - 100 mg
     - 4
     - 3.00
   * - 50 mg
     - 1
     - 1.33
   * - 50 mg
     - 2
     - 1.33
   * - 50 mg
     - 1
     - 1.33
