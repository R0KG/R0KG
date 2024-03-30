

# Aufgabe 2.1
$url = 'https://tiss.tuwien.ac.at/api/person/v22/id/384099'

$response = Invoke-RestMethod -Method Get -Uri $url



$first_name = $response.first_name
$last_name = $response.last_name
$fullName = $first_name + ' ' + $last_name
$org_list = $response.employee  

$depth = 0


$htmlOutput = @"
<html>
<head>
  <title>$fullName</title>
  <link rel="stylesheet" type="text/css" href="./TISS REST-API Dokumentation _ TU Wien_files/basic.css">
</head>
<body>
  <h1>$fullName</h1>
  <ul>
"@


foreach ($unit in $org_list) {
    $orgRef = $unit.org_ref
    $tiss_id = $orgRef.tiss_id
    $code = $orgRef.code
    $german = $orgRef.name_de
    $english = $orgRef.name_en


    $depth += 1 
    $depthDashes = "-" * $depth
    
    $listItem = @"
    
    <li>
      <strong>Depth:</strong> $depthDashes
      <strong>Code:</strong> $code
      <strong>TISS ID:</strong> $tiss_id
      <strong>German:</strong> $german
      <strong>English:</strong> $english
    </li>

"@
    $htmlOutput += $listItem
}


$htmlOutput += @"
  </ul>
</body>
</html>
"@


$htmlOutput | Out-File -FilePath .\data.html




