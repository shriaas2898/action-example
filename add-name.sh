n=1
while read line; do
if [[ $line =~ "End of Leaderbaord" ]]
then
   echo $n
   sed -i "${n}iHello $USERNAME" README.md
   break
fi
n=$((n+1))
done < "README.md"

