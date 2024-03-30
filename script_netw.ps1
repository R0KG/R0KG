# Set the target DNS server
$DNSServer = "8.8.8.8"

# Create a directory to store the captured results
$OutputDir = "dns_capture_results"
New-Item -ItemType Directory -Force -Path $OutputDir

# Loop to perform DNS queries and save the results
while ($true) {
    $Timestamp = Get-Date -Format "yyyyMMddHHmmss"
    $OutputFile = Join-Path -Path $OutputDir -ChildPath "dns_query_$Timestamp.txt"

    # Perform DNS queries and store the results
    Resolve-DnsName -Name youtube.com -Server $DNSServer | Format-Table | Out-File -Append -FilePath $OutputFile

    # Pause for a while before the next query (adjust the sleep duration as needed)
    Start-Sleep -Seconds 3600  # Sleep for 1 hour
}
