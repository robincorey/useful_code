# php file extension lets interpreter know php to be expected
# but the rest of the script can be html
# comment can also be //

<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
        <p>
          <?php                           # so <?php is start php stuff
            echo "Big" . " " . "balls";   # . is concatenate strings. semicolons at end of each statement, natch
            $myVar = "Tummos";            # to define variable
            $myIntVar = 23;               # int
            if($myIntVar > 5) {
              echo "bigger than 5";
            }
             
          ?>                              # some weird way of finsihing html php tag
        </p>
	</body>
</html>
