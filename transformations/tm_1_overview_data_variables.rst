.. sectionauthor:: Laiton Hedley

.. _data-variables:

==============
Data Variables
==============

All data you bring into or enter directly in jamovi starts as **Data Variables**.
These columns form the raw data used as the basis for your analyses. Opening a
dataset (such as a .csv file) or typing values into the spreadsheet creates these
variables automatically.

Measure and Data Types
----------------------

Every variable in jamovi has a **Measure type** and a **Data type** that
indicate the kind of data it contains and how it should be treated in analyses.

Data types can be:

- **Integer**: whole numbers without decimal points.
- **Decimal**: numbers with decimal points.
- **Text**: text, words, or categories (strings).

.. note::
   jamovi does not support a native date and time data type at this time.
   You can represent dates and times as text and use a number of date
   manipulations — see :doc:`tm_9_date_handling` for details.

Measure types indicate the `level of measurement <https://en.wikipedia.org/wiki/Level_of_measurement>`__:

- |continuous_icon| **Continuous**: Numbers where a continuum of values is meaningful, such as height, weight, or counts.
- |ordinal_icon| **Ordinal**: Discrete values where order is meaningful (e.g., 'Strongly agree', 'Agree' or '< 18', '18–30').
- |nominal_icon| **Nominal**: Discrete values with no meaningful order (e.g., Male, Female or 'Smoker', 'Non-smoker').
- |id_icon| **ID**: Unique identifiers for each row or participant (e.g., participant numbers or names).

jamovi combines *ratio* and *interval* into the **Continuous** measure type.
The **ID** type is useful for identifiers you don't usually analyse, as it
improves performance with large datasets.

.. note::
   Not all combinations of data type and measure type are valid. For example,
   a variable cannot be both Text and Continuous, or Decimal and Nominal.

When you bring in data, jamovi automatically assigns these types based on the
content. If the automatic assignment isn't what you need, you can adjust it
manually.

Double-click a column header to open the **variable editor**. From here, you
can see and modify the variable's name, description, data type, and measure type.

For example, if a variable representing a performance percentage incorrectly
appears as Nominal with an Ordinal measure type:

|data_var_editor|

1. Click the **Measure type** to open the drop-down menu and select **Continuous**.
2. Click the **Data type** and select **Decimal**.

|data_var_editor_part_two|

jamovi now treats this variable as continuous, allowing you to use it in
analyses like correlation or regression, or in mathematical operations like
computing a z-score.

Missing Values
--------------

In jamovi, missing values are represented as blank cells in the data view.

If your dataset uses special values to encode missing data (like -99 or 9999),
analyses will treat them as actual values unless you instruct jamovi otherwise.
To do this:

1. Open the **variable editor** by double-clicking the column header.
2. Click **Missing values**.
3. Click **Add Missing Value**.
4. Specify whether to treat values that are equal to, less than, or greater
   than a number as missing.

For example, to treat any value equal to 9999 as missing, use the formula ``== 9999``:

|data_var_editor_missing_vals|

Adding Labels to Levels
-----------------------

For Nominal or Ordinal variables, you can add descriptive labels to the levels.
This makes your output much easier to read. Below is a variable called "Group"
using numeric codes:

.. list-table:: Example of a Variable with Unlabeled Levels
   :header-rows: 1

   * - ID
     - Group
   * - 1
     - 1
   * - 2
     - 2
   * - 3
     - 1
   * - 4
     - 2

In this case, 1 represents "Smoker" and 2 represents "Non-smoker". To assign
these labels, open the **variable editor**:

|data_var_recode_one|

Click on the current levels (1 and 2) and type the meaningful labels:

|data_var_recode_two|

The variable now displays these labels in all analyses and results:

.. list-table:: Example of a Variable with Labeled Levels
   :header-rows: 1

   * - ID
     - Group
   * - 1
     - Smoker
   * - 2
     - Non-smoker
   * - 3
     - Smoker
   * - 4
     - Non-smoker

Reordering Levels
-----------------

For Ordinal (and sometimes Nominal) variables, you can reorder the levels so
they appear intuitively in tables and figures.

For example, if "Task Difficulty" levels appear in the wrong order:

.. list-table:: Descriptives Table with Levels Unordered
   :header-rows: 1

   * - Task Difficulty
     - Mean
     - Standard Deviation
   * - Low
     - 85.1
     - 9.5
   * - High
     - 54.3
     - 9.1
   * - Medium
     - 73.6
     - 9.3

1. Double-click the variable header to open the **variable editor**.
2. Click a level in the list and use the arrow keys to move it.

|ts_table_reorder_me|

The level at the top of the list will appear first (leftmost or topmost) in all
tables and figures:

|ts_table_reordered|

The table now displays levels in the natural order: Low, Medium, High.

.. list-table:: Descriptives Table with Levels Reordered
   :header-rows: 1

   * - Task Difficulty
     - Mean
     - Standard Deviation
   * - Low
     - 85.1
     - 9.5
   * - Medium
     - 73.6
     - 9.3
   * - High
     - 54.3
     - 9.1

Retain Unused Levels in Analyses
--------------------------------

If a categorical variable has valid levels that don't appear in your current
data, you can still include them in your reporting.

For example, if you ask Adult and Child moviegoers if they enjoyed a film and
everyone answers "Yes", the "No" level is absent but still relevant.

.. list-table:: Example Data with an Unused Level
   :header-rows: 1

   * - Age Group
     - Enjoyed Film (Y/N)
   * - Adult
     - Yes
   * - Adult
     - Yes
   * - Adult
     - Yes
   * - Child
     - Yes
   * - Child
     - Yes
   * - Child
     - Yes

To retain the "No" level in your tables:

1. Open the **variable editor**.
2. Click the plus sign (+) at the bottom of the levels list.
3. Type "No" to add the level.
4. Click the **Retain unused levels in analyses** toggle.

|ts_unused_level|

|ts_unused_level_part_two|

|ts_retain_unused_level|

The "No" level will now appear in your tables and figures even with no
matching participants.


.. |continuous_icon| image:: /_images/variable-continuous.svg
   :alt: Continuous measure type icon
   :height: 18px

.. |nominal_icon| image:: /_images/variable-nominal.svg
   :alt: Nominal measure type icon
   :height: 18px

.. |ordinal_icon| image:: /_images/variable-ordinal.svg
   :alt: Ordinal measure type icon
   :height: 18px

.. |id_icon| image:: /_images/variable-id.svg
   :alt: ID measure type icon
   :height: 18px

.. |data_var_editor| image:: /_images/ts_var_types_part_one.png
   :alt: The variable editor in jamovi showing incorrect measure and data types.
   :class: centered
   :width: 600px

.. |data_var_editor_part_two| image:: /_images/ts_var_types_part_two.png
   :alt: The variable editor in jamovi after correcting the measure and data types.
   :class: centered
   :width: 600px

.. |data_var_editor_missing_vals| image:: /_images/ts_missing_val.png
   :alt: The variable editor in jamovi showing a missing value rule set to == 9999.
   :class: centered
   :width: 600px

.. |data_var_recode_one| image:: /_images/ts_recode_one.png
   :alt: The variable editor showing unlabeled levels 1 and 2.
   :class: centered
   :width: 600px

.. |data_var_recode_two| image:: /_images/ts_recode_two.png
   :alt: The variable editor after assigning labels Smoker and Non-smoker.
   :class: centered
   :width: 600px

.. |ts_table_reordered| image:: /_images/ts_reordered_table.png
   :alt: The variable editor showing levels reordered to Low, Medium, High.
   :class: centered
   :width: 600px

.. |ts_table_reorder_me| image:: /_images/ts_unordered_table.png
   :alt: The variable editor showing levels in the unintuitive order Low, High, Medium.
   :class: centered
   :width: 600px

.. |ts_unused_level| image:: /_images/ts_add_unused_level.png
   :alt: The variable editor showing the plus button to add an unused level.
   :class: centered
   :width: 600px

.. |ts_unused_level_part_two| image:: /_images/ts_add_unused_level_part_2.png
   :alt: The variable editor after typing the unused level No.
   :class: centered
   :width: 600px

.. |ts_retain_unused_level| image:: /_images/ts_retain_unused_level.png
   :alt: The variable editor with the Retain unused levels in analyses toggle enabled.
   :class: centered
   :width: 600px
