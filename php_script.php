$input_excel_file_path = 'path/to/input/excel/file.xlsx';
$output_excel_file_path = 'path/to/output/excel/file.xlsx';

$command = "python3 /path/to/python/script.py '{$input_excel_file_path}' '{$output_excel_file_path}'";
$output = exec($command);

echo "Output Excel file path: " . $output;