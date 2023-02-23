# To print bash var in awk
bashvar=7
awk -v var="$bashvar" '{print $var}'`

# To find all files containg string, and filter by file type
find . -type f -print0 | xargs -0 grep -l "Distance" -R --include=*.top

## To reduce a long data file
awk 'NR ==1 || NR % 1000 == 0' big.xvg > small.xvg

# moving only certain files (in this case keeping *comp.xtc and moving 'noncomp'*.xtc
if [ ! -d "todelete" ]; then mkdir "todelete"; fi; list=(*.*); for i in `seq 0 200`; do if [[ ! ${list[i]} == *"comp"* ]] && [[ ${list[i]} == *".xtc"* ]]; then mv ${list[i]} todelete; fi; done

# reading in multi vars from an awk command
read -r x y z < <(grep "OD1 ASN A 237" lig_out.pdb | awk '{print $7,$8,$9}') ; echo $x $y $z
