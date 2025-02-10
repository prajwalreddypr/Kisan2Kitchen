
<?php
// Define the input file name
$input_file = 'glcm_features.xlsx';

// Call the Python script to update the Excel file
$output_file = exec("python step2.py $input_file");

// Use the output file name as required
echo "Updated file saved as: $output_file";

?>