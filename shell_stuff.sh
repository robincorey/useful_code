# To print bash var in awk
bashvar=7
awk -v var="$bashvar" '{print $var}'`
