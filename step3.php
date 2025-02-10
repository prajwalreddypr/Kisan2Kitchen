<?php
// Define input and output file paths
$input_file = "updated_new_excel_file.xlsx";
$output_file = "final.xlsx";

// Call Python script with input and output file paths as arguments
$command = escapeshellcmd("python step3.py $input_file $output_file");
$output = shell_exec($command);

// Print the output of the Python script
echo $output;
?>
