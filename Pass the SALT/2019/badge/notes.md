## Internal notes...

### Export attendees list 

* https://pretix.eu/control/event/passthesalt/2019/orders/export/
* Orders/Export/Order Data/Order positions - CSV (with semicolons)
* => 20190602_orders.csv

```
cat 20190602_orders.csv|grep -v "^Order"|gawk -F";" '{sub(/$/," ", $12);sub(/ /,"#",$12);sub(/ $/,"",$12);print $1 "#" $12 "#" $17 "#" $20}'|sed "s/'@/@/g"|grep "#No$"|sed 's/#No$//'|sort> 20190602_list0UK.txt
cat 20190602_orders.csv|grep -v "^Order"|gawk -F";" '{sub(/$/," ", $12);sub(/ /,"#",$12);sub(/ $/,"",$12);print $1 "#" $12 "#" $17 "#" $20}'|sed "s/'@/@/g"|grep -v "#No$"|sed 's/#[^#]*$//'|sort> 20190602_list0FR.txt
```

### Get strange chars

```
cat 20190602_list1*.txt|tr -d "a-zA-Z# 0-9"|sed 's/\(.\)/\1\n/g'|sort|uniq|tr -d '\n'
!'-./;=@_⠇⠈⠖⠞⠠⠢⠨⠵ćçéëîïôúü
```

### Spot long fields

```
cat 20190602_list1FR.txt|egrep "(#..............*#.*#|#.*#..............*#|#.*#.*#..............*)" |sort > 20190602_list1FRlong.txt
cat 20190602_list1UK.txt|egrep "(#..............*#.*#|#.*#..............*#|#.*#.*#..............*)" |sort > 20190602_list1UKlong.txt
cat 20190602_list1UK.txt|egrep -v "(#..............*#.*#|#.*#..............*#|#.*#.*#..............*)" |sort > 20190602_list1UKcourt.txt
cat 20190602_list1FR.txt|egrep -v "(#..............*#.*#|#.*#..............*#|#.*#.*#..............*)" |sort > 20190602_list1FRcourt.txt
```

### Manual fixes

Fix word capitalisation, spot missing ones:

```
cat 2019*_list1FR.txt 2019*_list1UK.txt |grep "#[A-Z][A-Z].*#"
```

### SVG

See [description.md](description.md)

Do a few empty badges too, do sponsor badges for still available vouchers

### Lanyard

https://mspie.com/produit/tour-de-cou-double-attacha-mousqueton/

### Generate cross-ref lists

```
cat 20190602_list1FRextra.txt 20190602_list1FR.txt  20190602_list1UK.txt |sort > 20190602_list.txt 
awk -F "#" 'BEGIN{OFS="#"}{print $1,$3,$2,$4}' 20190602_list.txt > 20190602_listB.txt
awk -F "#" 'BEGIN{OFS="#"}{print $1,$4,$2,$3}' 20190602_list.txt > 20190602_listC.txt
cat 20190602_list.txt 20190602_listB.txt 20190602_listC.txt|sort -t"#" -k2|sed 's/##/#/g;s/#$//'|uniq|sed 's/#/ # /g' > 20190602_list_all.txt
```
