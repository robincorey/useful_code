# php file extension lets interpreter know php to be expected
# but the rest of the script can be html
# comment can also be //
# WHITESPACE BELOW IS AWFUL!! Too much copy paste...

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
            if ($myIntVar > 5) {
              echo "bigger than 5";
            }
	    elseif (1>3) {
              echo "nowt";
            }
            else {
              echo "poo";
	    }
            ### switch works same way    
            switch (2) {
                case 0:
            echo 'The value is 0';
            break;
                case 1:
            echo 'The value is 1';
            break;
                case 2:
            echo 'The value is 2';
            break;
                default:
            echo "The value isn't 0, 1 or 2";
             }
             # another one
             $fruit = "Apple";
             switch ($fruit) {
                case 'Apple':
                echo "Yummy.";
                break;
              default:
                echo "Poo";
              }
                    $i = 5;
             # combining switches
             switch ($i) {
                case 0:
                echo '$i is 0.';
                break;
             case 1:
             case 2:
             case 3:
             case 4:
             case 5:
                echo '$i is somewhere between 1 and 5.';
                break;
             }
          ?>                              # some weird way of finsihing html php tag
        </p>
	</body>
</html>

