.. sectionauthor:: Laiton Hedley


.. _list-of-functions:

=================
List of Functions
=================

Use these functions in the formula editor to create computed variables,
transformed variables, and filters.

Understanding Formulas
----------------------

Build your formulas using numbers, variable names, text values, operators, and
functions.

- **Numbers**: Enter whole numbers or decimals as-is (e.g., ``1``, ``2.5``).
- **Variable names**: Type the name of an existing column (e.g., ``variable_name``).
- **Text values**: Wrap text in single quotes (e.g., ``'Yes'``, ``'Group A'``).
- **Operators**: Use arithmetic operators (``+``, ``-``, ``*``, ``/``) or
  logical operators (``and``, ``or``).

.. tip::
   If a variable name contains spaces, wrap it in backticks so jamovi can
   parse it correctly (e.g., use \`reaction time\`).

Row vs. Variable Functions
--------------------------

Many functions come in two versions:

- **Row functions** (e.g., ``MEAN``): Use these to calculate a result for each
  row individually.
- **Variable functions** (e.g., ``VMEAN``): Use these to perform a calculation
  using every value in a column.

For more detail on this distinction, see :doc:`tm_4_row_v_functions`.

Math Functions
--------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``ABS(var)``
     - Calculate the absolute value of each number in the column.
     - `Info <https://en.wikipedia.org/wiki/Absolute_value>`__
   * - ``EXP(var)``
     - Raise *e* to the power of each value in the column.
     - `Info <https://en.wikipedia.org/wiki/Exponential_function>`__
   * - ``LN(var)``
     - Calculate the natural logarithm (base *e*) of each value.
     - `Info <https://doi.org/10.1177/00045632211050531>`__
   * - ``LOG10(var)``
     - Calculate the base-10 logarithm of each value.
     - `Info <https://doi.org/10.1177/00045632211050531>`__
   * - ``SQRT(var)``
     - Calculate the square root of each value.
     - `Info <https://en.wikipedia.org/wiki/Square_root>`__

Statistical Functions
---------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``ABSIQR(var)``
     - Calculate the average absolute deviation of values from the median.
     - `Info <https://en.wikipedia.org/wiki/Interquartile_range>`__
   * - ``ABSZ(var)``
     - Calculate the absolute z-score for each value.
     - `Info <https://en.wikipedia.org/wiki/Standard_score>`__
   * - ``BOXCOX(var)``
     - Apply a Box-Cox transformation to the variable.
     - `Info <https://en.wikipedia.org/wiki/Power_transform#Box%E2%80%93Cox_transformation>`__
   * - ``CEILING(var)``
     - Round up each value to the nearest whole number.
     - `Info <https://en.wikipedia.org/wiki/Floor_and_ceiling_functions>`__
   * - ``FLOOR(var)``
     - Round down each value to the nearest whole number.
     - `Info <https://en.wikipedia.org/wiki/Floor_and_ceiling_functions>`__
   * - ``IQR(var)``
     - Identify if a value is within the "box" (0) or outside the "whiskers" (> 1.5).
     - `Info <https://en.wikipedia.org/wiki/Interquartile_range>`__
   * - | ``MAX(...)``
       | ``VMAX(...)``
     - Find the highest value in a row (``MAX``) or column (``VMAX``).
     - `Info <https://en.wikipedia.org/wiki/Maximum_and_minimum>`__
   * - ``MAXABSIQR(var)``
     - Find the maximum absolute interquartile range across multiple variables.
     - `Info <https://en.wikipedia.org/wiki/Interquartile_range>`__
   * - ``MAXABSZ(var)``
     - Find the maximum absolute z-score across multiple variables.
     - `Info <https://en.wikipedia.org/wiki/Standard_score>`__
   * - | ``MEAN(...)``
       | ``VMEAN(...)``
     - Calculate the average of a row (``MEAN``) or an entire column (``VMEAN``).
     - `Info <https://en.wikipedia.org/wiki/Mean>`__
   * - | ``MIN(...)``
       | ``VMIN(...)``
     - Find the lowest value in a row (``MIN``) or column (``VMIN``).
     - `Info <https://en.wikipedia.org/wiki/Maximum_and_minimum>`__
   * - ``RANK(var)``
     - Assign an ordinal rank to each value in the column.
     - `Info <https://en.wikipedia.org/wiki/Ranking_(statistics)>`__
   * - ``ROUND(var, n)``
     - Round each value to *n* decimal places.
     - `Info <https://en.wikipedia.org/wiki/Rounding>`__
   * - ``SCALE(var)``
     - Normalize a set of numbers (shorthand for ``Z(var)``).
     - `Info <https://en.wikipedia.org/wiki/Standard_score>`__
   * - | ``STDEV(...)``
       | ``VSTDEV(...)``
     - Calculate the standard deviation of a row (``STDEV``) or column (``VSTDEV``).
     - `Info <https://en.wikipedia.org/wiki/Standard_deviation>`__
   * - | ``SUM(...)``
       | ``VSUM(...)``
     - Add up all values in a row (``SUM``) or column (``VSUM``).
     - `Info <https://en.wikipedia.org/wiki/Summation>`__
   * - ``VMAD(var)``
     - Calculate the median absolute deviation of a variable.
     - `Info <https://en.wikipedia.org/wiki/Median_absolute_deviation>`__
   * - ``VMADR(var)``
     - Calculate the robust median absolute deviation of a variable.
     - `Info <https://en.wikipedia.org/wiki/Median_absolute_deviation>`__
   * - ``VMED(var)``
     - Find the median of a variable.
     - `Info <https://en.wikipedia.org/wiki/Median>`__
   * - ``VMODE(var)``
     - Find the most common value (mode) in a variable.
     - `Info <https://en.wikipedia.org/wiki/Mode_(statistics)>`__
   * - ``VN(var)``
     - Return the number of non-missing cases in a variable (sample size).
     - `Info <https://en.wikipedia.org/wiki/Sample_size_determination>`__
   * - ``VSE(var)``
     - Calculate the standard error of a variable.
     - `Info <https://en.wikipedia.org/wiki/Standard_error>`__
   * - | ``VAR(...)``
       | ``VVAR(...)``
     - Calculate the variance of a row (``VAR``) or column (``VVAR``).
     - `Info <https://en.wikipedia.org/wiki/Variance>`__
   * - ``Z(var)``
     - Standardize values into z-scores.
     - `Info <https://en.wikipedia.org/wiki/Standard_score>`__

Logical Functions
-----------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``IF(cond, val, else)``
     - If the condition is true, use *val*; otherwise, use *else*.
     - `Info <https://en.wikipedia.org/wiki/Conditional_(computer_programming)>`__
   * - ``IFMISSING(v, val, else)``
     - Use *val* if the cell is empty; otherwise, use *else*.
     - `Info <https://en.wikipedia.org/wiki/Conditional_(computer_programming)>`__
   * - ``NOT(var)``
     - Invert a boolean value (True becomes False, and vice versa).
     - `Info <https://en.wikipedia.org/wiki/Negation>`__

Text Functions
--------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``CONTAINS(needle, hay)``
     - Check if a specific string (the needle) exists in a variable (the haystack).
     - `Info <https://en.wikipedia.org/wiki/String_searching_algorithm>`__
   * - ``SPLIT(v, 'by', pos)``
     - Split a text string by a specific character and return the text at a given position.
     - `Info <https://en.wikipedia.org/wiki/String_(computer_science)>`__
   * - ``TEXT(var)``
     - Convert numeric values into text format.
     - `Info <https://en.wikipedia.org/wiki/String_(computer_science)>`__
   * - ``VALUE(var)``
     - Convert text strings into numeric values, if possible.
     - `Info <https://en.wikipedia.org/wiki/String_(computer_science)>`__

Date and Time Functions
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``DATEVALUE(var)``
     - Convert a text date (e.g., 2000-12-20) into the number of days since 1 Jan 1970.
     - `Info <https://en.wikipedia.org/wiki/Unix_time>`__
   * - ``DATE(var)``
     - Convert a Unix day count back into a formatted date string.
     - `Info <https://en.wikipedia.org/wiki/Unix_time>`__

Reference Functions
-------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``HLOOKUP(idx, v1, v2, ...)``
     - Retrieve values from specific rows using a provided index.
     - `Info <https://en.wikipedia.org/wiki/Lookup_table>`__
   * - ``MATCH(var, val1, ...)``
     - Find the row index of the first value that matches your criteria.
     - `Info <https://en.wikipedia.org/wiki/Lookup_table>`__

Miscellaneous Functions
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``COUNT(var)``
     - Count the number of non-missing values in a set of columns.
     - `Info <https://en.wikipedia.org/wiki/Counting>`__
   * - ``FILTER(var, expression)``
     - Return only the values in a column that meet a specific condition.
     - `Info <https://en.wikipedia.org/wiki/Filter_(higher-order_function)>`__
   * - ``INT(var)``
     - Strip the fractional component from a number to make it an integer.
     - `Info <https://en.wikipedia.org/wiki/Integer>`__
   * - ``OFFSET(var, n)``
     - Shift the data in a column up or down by *n* rows.
     - `Info <https://en.wikipedia.org/wiki/Offset_(computer_science)>`__
   * - ``ROW()``
     - Fill a column with the current row number.
     -
   * - ``SAMPLE(var, n)``
     - Draw a random sample of *n* values from a variable.
     - `Info <https://en.wikipedia.org/wiki/Sampling_(statistics)>`__
   * - ``VROWS(var)``
     - Return the total number of rows in a variable.
     -

Simulation Functions
--------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 10

   * - Function
     - Description
     -
   * - ``BETA(alpha, beta)``
     - Draw random samples from a Beta distribution.
     - `Info <https://en.wikipedia.org/wiki/Beta_distribution>`__
   * - ``GAMMA(shape, scale)``
     - Draw random samples from a Gamma distribution.
     - `Info <https://en.wikipedia.org/wiki/Gamma_distribution>`__
   * - ``NORM(mean, stdev)``
     - Draw random samples from a Normal (Gaussian) distribution.
     - `Info <https://en.wikipedia.org/wiki/Normal_distribution>`__
   * - ``UNIF(min, max)``
     - Draw random samples from a Uniform distribution.
     - `Info <https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)>`__
