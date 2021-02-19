# script that fixes the typo that was breaking apache
exec { 'fix':
    command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
    provider => "shell"
}
