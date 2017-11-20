use strict; # strict variables
use warnings;

# perl awesome at reading files
open RFILE,"<$filename" or die "Cannot read from $filename: $!\n";

# perl also awesome at writing files
open WFILE,">$numbered_filename" or die "Cannot write to $numbered_filename: $!\n";
#nb die is super useful.

# read lines of a file
while ($line = <RFILE>)
{
    $i = $i + 1;

    print WFILE "$i : $line";
}

# match string ("a")
$line =~ m/a/;

# sed stuff
$line =~ s/the/THE/g;

# uses backticks like shell
@files = `ls $directory`;
# @ is an array I guess

# if loops
my $fragment = "APC";

if ($fragment =~ m/P/) { 
    my $propensity = "Hello";   
}
