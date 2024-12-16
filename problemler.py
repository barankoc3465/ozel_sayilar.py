# sayi = int(input("Bir sayı giriniz: "))
# for i in range(2,sayi+1):
#     if sayi%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,"Sayısı",sayi,"Sayısının Asal Çarpanıdır.")


# sayi=int(input("Bir sınır tuşlayınız: "))
# for i in range(2,sayi+1):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"monkey d. luffy")
#             break
#     else:
#         print(i,"Sayısı Asal Sayıdır.")


# sayi=input("Bir sayı tuşlayınız: ")
# toplam=0
# for i in sayi:
#     toplam=toplam+int(i)**3
# if toplam==int(sayi):
#     print("Sayı armstrong sayısıdır.")
# else:
#     print("Değildir.")


# sayi=input("Bir sayı tuşlayın: ")
# toplam=0
# for i in sayi:
#     toplam+=int(i)
# if int(sayi)%toplam==0:
#     print("Sayı Harshad (Niven) Sayısıdır.")
# else:
#     print("Değildir.")


# sayi=int(input("Bir sayı tuşlayıınz: "))
# karekok=sayi**0.5
# karekok2=int(karekok)
# if karekok==karekok2:
#     for i in range(2,karekok2):
#         if karekok2%i==0:
#                 break
#     else:
#         print(sayi,"Sayısı karekök asal sayıdır.")
# else:
#     print(sayi,"Sayısı karekök asal sayı değildir.")


# kelime=input("Bir sayı giriniz: ")
# frp=""
# for i in kelime:
#     frp=i+frp
# if frp==kelime:
#     print(kelime,"Sayısı polindrom sayıdır.")
# else:
#     print("Değildir.")


# sayi=int(input("Bir giriniz: "))
# asal_bolen_listesi=""
# for i in range(2,sayi+1):
#     if sayi%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             if str(i) not in asal_bolen_listesi:
#                 asal_bolen_listesi+=" "+str(i)
#                 continue
# print(asal_bolen_listesi)


# sayi=input("Bir giriniz: ")
# asal_bolen_listesi=""
# asal_sayilar_toplami=0
# rakamlar=""
# rakamlar_toplami=0
# for l in sayi:
#     rakamlar+=" "+str(l)
#     rakamlar_toplami+=int(l)
# for i in range(2,int(sayi)+1):
#     if int(sayi)%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             if str(i) not in asal_bolen_listesi:
#                 asal_bolen_listesi+=" "+str(i)
#                 asal_sayilar_toplami+=i
#                 continue
# print("Asal Çarpanlar: ",asal_bolen_listesi)
# print("Rakamlar: ",rakamlar)
# print("Asal çarpanların toplamı: ",asal_sayilar_toplami)
# print("Rakamlar Toplamı: ",rakamlar_toplami)
# if asal_sayilar_toplami==rakamlar_toplami:
#     print(sayi+"Sayısı Smith Sayısıdır.")
# else:
#     print(sayi+" Sayısı Smith Sayısı değildir.")


# sayi=int(input("Bir sayı giriniz: "))
# basamak_sayisi=0
# basamak_sayilarinin_uslerinin_toplami=0
# for i in str(sayi):
#     basamak_sayisi+=1

# for sayilar in str(sayi):
#     basamak_sayilarinin_uslerinin_toplami+=int(sayilar)**basamak_sayisi
# if basamak_sayilarinin_uslerinin_toplami==sayi:
#     print(sayi,"Sayısı Perfect Digital Invariant (PDİ) Sayısıdır.")
# else:
#     print(sayi,"Sayısı Perfect Digital Invariant (PDİ) Sayısı Değildir.")


# sayi=int(input("Bir sayı giriniz: "))
# a,b=0,1
# fibbonacci=str(a)
# for i in range(sayi+1):
#     a,b=b,a+b
#     if a>sayi:
#         break
#     else:
#         fibbonacci+=","+str(a)
# print(fibbonacci)


# sayi1=int(input("Bir sayı giriniz: "))
# sayi2=int(input("Bir sayı giriniz: "))
# toplam1=0
# toplam2=0
# for i in range(1,sayi1):
#     if sayi1%i==0:
#         toplam1+=i
# for j in range(1,sayi2):
#     if sayi2%j==0:
#         toplam2+=j
# if toplam1==sayi2 and toplam2==sayi1:
#     print(sayi1,"ve",sayi2,"Sayıları arkadaş sayılardır.")
# else:
#     print("bu sayılar arkadaş falan değiller...")


# sayi=int(input("Bir sayı giriniz."))
# sayi_karesi=sayi**2
# sayi_basamak=0
# sayi_karesi_tersi_sayi_basamak=0
# sayi_karesi_tersi=""
# tersten_yeni_sayi=""
# ters_sayi=""
# for i in str(sayi):
#     sayi_basamak+=1
#     ters_sayi=i+ters_sayi
# print(sayi_basamak)
# for j in str(sayi_karesi):
#     sayi_karesi_tersi=j+sayi_karesi_tersi
# print(sayi_karesi_tersi)
# for k in sayi_karesi_tersi:
#     tersten_yeni_sayi+=k
#     sayi_karesi_tersi_sayi_basamak+=1
#     if sayi_karesi_tersi_sayi_basamak==sayi_basamak:
#         break
# print(tersten_yeni_sayi)
# print(sayi_karesi_tersi_sayi_basamak)
# if tersten_yeni_sayi==ters_sayi:
#     print(sayi,"Sayısı Automorphic Sayılar Aşiretindendir.")
# else:
#     print(sayi,"Sayısı Automorphic Sayılar Aşiretinden değildir...")


# birikim=""
# sayi=int(input("Bir sayı giriniz: "))
# for i in range(1,sayi+1):
#     ucgen_sayılar=i*(i+1)/2
#     print(int(ucgen_sayılar))


# sayi=int(input("Bir sayı giriniz: "))
# rakamların_faktoriyellerinin_toplamı=0
# for i in str(sayi):
#     faktoriyel=1
#     for j in range(1,int(i)+1):
#         faktoriyel*=j
#     rakamların_faktoriyellerinin_toplamı+=faktoriyel
# if rakamların_faktoriyellerinin_toplamı==sayi:
#     print(sayi,"Sayısı Factorion Sayıları Ailesinin Bir Üyesidir.")
# else:
#     print(sayi,"Sayısı Factorion Sayıları Ailesinin Bir Üyesi Değildir...")


# sayi1=int(input("Bir sayı giriniz: "))
# sayi2=int(input("Bir sayı giriniz: "))
# bolenler_toplamı1=0
# bolenler_toplamı2=0
# for i in range(1,sayi1+1):
#     if sayi1%i==0:
#         bolenler_toplamı1+=i
# for j in range(1,sayi2+1):
#     if sayi2%j==0:
#         bolenler_toplamı2+=j
# oran2=bolenler_toplamı2/sayi2
# oran1=bolenler_toplamı1/sayi1
# print(oran1,oran2)
# if oran1==oran2:
#     print(sayi1,"ve",sayi2,"Çift Dost Sayılardır. (Friendly Numbers)")
# else:
#     print(sayi1,"ve",sayi2,"Çift Dost Sayılar Değillerdir... (Friendly Numbers)")


# sayi=int(input("Bir sınır sayısı giriniz: "))
# a,b=0,1
# for i in range(1,sayi):
#     print(a)
#     a,b=b,a+b


# sayi=int(input("bir sayı giriniz: "))
# adet=0
# a,b,c="","",""
# for i in str(sayi):
#     if a=="":
#         a=i
#     elif b=="":
#         b=i
#     elif c=="":
#         c=i
# a,b,c=int(a),int(b),int(c)
# for j in range(sayi):
#     print(a)
#     a,b,c=b,c,a+b+c
#     if a==sayi:
#         print(sayi,"Sayısı 3 Basamaklı Keith Ailesinin Bir üyesidir.")
#         break
#     elif a>sayi:
#         print(sayi,"Sayısı 3 Basamaklı Keith Ailesinin Bir üyesi değildir...")
#         break


# n=int(input("Bir sayı giriniz: "))
# e=0
# for i in range(n):
#     faktoriyel=1
#     for j in range(1,n+1):
#         faktoriyel*=j
#     else:
#         e+=1/faktoriyel
# print(e,"Sayısı Euler Sayısıdır.")


# sayi=int(input("Bir sınır değer belirleryiniz: "))
# pn=0
# pentagonal_sayilar=""
# for i in range(1,sayi+1):
#     pn+=i*(3*i-1)/2
#     print(pn)


# sayi=input("Bir sayı giriniz: ")
# for i in range(150):
#     ters_sayi=""
#     for j in str(sayi):
#         ters_sayi=j+ters_sayi
#     if str(ters_sayi)!=str(sayi):
#         print("ters sayı",ters_sayi)
#         sayi=int(sayi)+int(ters_sayi)
#         print("yeni sayı",sayi)
#         continue
#     else:
#         print("Lychrel Sayısıdır.")
#         break
# else:
#     print("Lychrel Sayısı olabilir.")


# sayi=int(input("Bir sayı giriniz: "))
# asal_çarpım=1
# for i in range(2,sayi+1):
#     if sayi%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             asal_çarpım*=i
#             print(i)
            
# print(asal_çarpım,"")
# if sayi==asal_çarpım:
#     print(sayi,"Sayısı Primorial Sayıdır.")
# else:
#     print(sayi,"Sayısı Primorial Sayı değildir.")


# sayi=int(input("Bir sayı tuşlayınız: "))
# for i in range(2,sayi+1):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"asal değil")
#             break
#     else:
#         print(i,"asal")


# sayi=int(input("2' den büyük bir çift sayı tuşlayınız: "))
# for i in range(2,sayi+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         for k in range(2,sayi+1):
#             for l in range(2,k):
#                 if k%l==0:
#                     break   
#             else:
#                 print(i,k)
#                 if i+k==sayi:
#                     print(i,"Ve",k,"Asal sayılarının toplamı",sayi,"Sayısına eşittir.")
#                     print(sayi,"Sayısı Goldbach Varsayımına harfi harfine uyar.")
#                     break


# sayi=int(input("Bir sayı tuşlayınız: "))
# adet=0
# adet2=0 
# for i in str(sayi):
#     adet+=1
# for j in range(1,adet+1):
#     if str(j) in str(sayi):
#         adet2+=1
# if adet2==adet:
#     print(sayi,"Sayısı Pandigital Sayılardandır.")
# else:
#     print(sayi,"Sayısı Pandigital Sayılardan değildir.")


# sayi=int(input("Bir sayı giriniz: "))
# a=sayi
# adim=0
# while True:
#     if sayi%2==0:
#         sayi/=2
#         print(int(sayi))
#     else:
#         sayi=sayi*3+1
#         print(int(sayi))
#     adim+=1
#     if sayi==1:
#         break
# print(a,"Sayısı Collatz Dizisine",adim,"adımda ulaşmıştır.")


# baslangıc=int(input("Aralığınızın başlangıç değerini belirleyiniz: "))
# bitis=int(input("Aralığınızın bitiş değerini belirleyiniz: "))
# for i in range(baslangıc,bitis+1):
#     ters_sayi=""
#     for j in str(i):
#         ters_sayi=j+ters_sayi
#         if ters_sayi==str(i):
#             print(i,"Polindrom sayıdır.")
#             break
#     for k in range(2,i):
#         if i%k==0:
#             print(i,"Asal değildir.")
#             break
#     else:
#         print(i,"Asaldır.")
#         if ters_sayi==str(i):
#             print(i,"Sayısı Polindromik Asal Sayıdır.")
#             continue


# baslangıc=int(input("Aralığınızın başlangıç değerini belirleyiniz: "))
# bitis=int(input("Aralığınızın bitiş değerini belirleyiniz: ")) 
# for i in range(baslangıc,bitis):
#     basamak_adedi=0
#     tam_bolen_adedi=0
#     for j in str(i):
#         basamak_adedi+=1
#         if int(j)==0:
#             break
#         if i%int(j)==0:
#             tam_bolen_adedi+=1
#     if basamak_adedi==tam_bolen_adedi:
#         print(i,"Sayısı Self-dividing Sayılarındandır.")
#     else:
#         print(i,"Sayısı Self-dividing Sayılarından değildir.")


# baslangıc=int(input("Aralığınızın başlangıç değerini yazınız: "))
# bitis=int(input("Aralığınızın bitiş değerini yazınız: "))
# adet=0
# for i in range(baslangıc,bitis):
#     faktoriyel1=1
#     faktoriyel2=1
#     faktoriyel3=1
#     adet+=1
#     for j in range(1,2*i+1):
#             faktoriyel1*=j
#     for k in range(1,i+2):
#             faktoriyel2*=k
#     for l in range(1,i+1):        
#             faktoriyel3*=l
#     catalan_sayisi=faktoriyel1/(faktoriyel2*faktoriyel3)
#     print(str(adet)+". Catalan Sayısı: ",catalan_sayisi)
   

# sayi=int(input("2' den büyük bir çift sayı tuşlayınız: "))
# for i in range(2,sayi+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#             adet=0
#             for l in range(2,sayi-i):
#                 if (sayi-i)%l==0:
#                     break   
#             else:
#                 print(i,l+1)
#                 if i+l+1==sayi:
#                     print(i,"Ve",sayi-i,"Asal sayılarının toplamı",sayi,"Sayısına eşittir.")
#                     print(sayi,"Sayısı Goldbach Varsayımına harfi harfine uyar.")


# sayi=int(input("2' den büyük bir çift sayı tuşlayınız: "))
# for i in range(2,sayi+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         for k in range(2,sayi+1):
#             for l in range(2,k):
#                 if k%l==0:
#                     break   
#             else:
#                 print(i,k)
#                 if i+k==sayi:
#                     print(i,"Ve",k,"Asal sayılarının toplamı",sayi,"Sayısına eşittir.")
#                     print(sayi,"Sayısı Goldbach Varsayımına harfi harfine uyar.")
#                     break


# baslangıc=int(input("Aralığınız için başlangıç değeri giriniz: "))
# bitis=int(input("Aralığınız için bitiş değeri giriniz: "))
# for i in range(baslangıc,bitis+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         rakamlar_toplami=0
#         print(i,"Sayısı asal sayıdır.")
#         for a in str(i):
#             rakamlar_toplami+=int(a)
#         print(rakamlar_toplami,"Sayısı",i,"Sayısının rakamları toplamıdır.")


# sayi=input("Bir giriniz: ")
# asal_bolen_listesi=""
# asal_sayilar_toplami=0
# rakamlar=""
# rakamlar_toplami=0
# for l in sayi:
#     rakamlar+=" "+str(l)
#     rakamlar_toplami+=int(l)
# for i in range(2,int(sayi)+1):
#     if int(sayi)%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             if str(i) not in asal_bolen_listesi:
#                 asal_bolen_listesi+=" "+str(i)
#                 asal_sayilar_toplami+=i
#                 continue
# print("Asal Çarpanlar: ",asal_bolen_listesi)
# print("Rakamlar: ",rakamlar)
# print("Asal çarpanların toplamı: ",asal_sayilar_toplami)
# print("Rakamlar Toplamı: ",rakamlar_toplami)
# if asal_sayilar_toplami==rakamlar_toplami:
#     print(sayi+"Sayısı Smith Sayısıdır.")
# else:
#     print(sayi+" Sayısı Smith Sayısı değildir.")


# sayi=int(input("Bir sayı giriniz: "))
# asal_mi=True
# for i in range(2,sayi):
#     if sayi%i==0:
#         asal_mi=False
#         break
# else:
#     asal_mi=True
#     print(sayi,"Sayısı Smith sayısı değildir.")
# if asal_mi==False:
#     rakamlar_toplami=0
#     asal_bolenler_toplami=0
#     asal_bolenler=""
#     asal_bolenler_carpımı=1
#     for rakam in str(sayi):
#         rakamlar_toplami+=int(rakam)
#     print(rakamlar_toplami,"Sayısı",sayi,"Sayısının rakamlarının toplamıdır.")
#     for j in range(2,sayi+1):
#         if sayi%j==0:
#             for k in range(2,j):
#                 if j%k==0:
#                     break 
#             else:
#                 asal_bolenler+=str(j)+" "
#                 asal_bolenler_carpımı*=j
#                 for m in str(j):
#                     asal_bolenler_toplami+=int(m)
# while True:
#     if sayi!=asal_bolenler_carpımı:
#         oran=sayi//asal_bolenler_carpımı
#         for a in range(2,oran+1):
#             if oran%a==0:
#                 for b in range(2,a):
#                     if a%b==0:
#                         break
#                 else:
#                     oran//=a
#                     asal_bolenler_carpımı*=a
#                     asal_bolenler_toplami+=a
#     else:
#         break
# if asal_bolenler_toplami==rakamlar_toplami:
#     print(asal_bolenler,sayi,"Sayıları",sayi,"Sayısının asal çarpanlarıdır.")
#     print(asal_bolenler_toplami,"Sayısı",sayi,"Sayısının asal çarpanlarının toplamıdır.")
#     print(sayi,"Sayısı Smith Sayısıdır.")
# else:
#     print(asal_bolenler,sayi,"Sayıları",sayi,"Sayısının asal çarpanlarıdır.")
#     print(asal_bolenler_toplami,"Sayısı",sayi,"Sayısının asal çarpanlarının toplamıdır.")
#     print(sayi,"Sayısı Smith Sayısıdır.")


# sayi=int(input("Bir sayı değeri giriniz: "))
# rakamlar_toplamı=0
# for i in range(2,sayi):
#     if sayi%i==0:
#        break
# else:
#     for rakam in str(sayi):
#         rakamlar_toplamı+=int(rakam)
#     for j in range(2,rakamlar_toplamı):
#         if rakamlar_toplamı%j==0:
#            break
#     else:
#         print(sayi,"ve",rakamlar_toplamı,"Sayısıları Asal Sayılardır.")
#         print(sayi,"Sayısı Mükemmel Sayıdır.")


# bitis=int(input("Aralığınız sınırı için bir tam sayı değeri giriniz: "))
# for a in range(2,bitis+1):
#     rakamlar_toplamı=0
#     for i in range(2,a):
#         if a%i==0:
#             break
#     else:
#         for rakam in str(a):
#             rakamlar_toplamı+=int(rakam)
#         for j in range(2,rakamlar_toplamı):
#             if rakamlar_toplamı%j==0:
#                 break
#         else:
#             print(a,"ve",rakamlar_toplamı,"Sayısıları Asal Sayılardır.")
#             print(a,"Sayısı Mükemmel Sayıdır.")



# bitis=int(input("Aralığınız sınırı için bir tam sayı değeri giriniz: "))
# for a in range(2,bitis+1):
#     rakamlar_toplami=0
#     for i in range(2,a):
#         if a%i==0:
#             break
#     else:
#         for rakam in str(a):
#             rakamlar_toplami2=0
#             rakamlar_toplami+=int(rakam)
#         for j in range(2,rakamlar_toplami):
#             if rakamlar_toplami%j==0:
#                 break
#         else:
#             for rakam2 in str(rakamlar_toplami):
#                 rakamlar_toplami2+=int(rakam2)
#             for k in range(2,rakamlar_toplami2):
#                 if rakamlar_toplami2%k==0:
#                     break
#             else:
#                 print(a,"Sayısı",rakamlar_toplami,"ve",rakamlar_toplami2,"Sayısıları Asal Sayılardır.")
#                 print(a,"Sayıları İkili Mükemmel Sayıdır.")


# bitis=int(input("Döngünüz için bir bitiş değeri belirleyiniz:"))
# narenci_sayilari_listesi=""
# for i in range(1,bitis+1):
#     basamaklarin_üssel_toplami=0
#     basamak_adedi=0
#     for k in str(i):
#         basamak_adedi+=1
#     for k in str(i):
#         basamaklarin_üssel_toplami+=int(k)**basamak_adedi
#     if basamaklarin_üssel_toplami==i:
#         narenci_sayilari_listesi+=str(i)+" "
# print(narenci_sayilari_listesi,"Sayıları 1'den",bitis,"'e kadar olan Narenci Sayılarıdır.")


# baslangıc=int(input("Aralığınız için bir Başlangıç değeri alınız: "))
# bitis=int(input("Aralığınız için bir Bitiş değeri alınız: "))
# harshad_niven_sayı_listesi=""
# for i in range(baslangıc,bitis+1):
#     basamak_toplami=0
#     for a in str(i):
#         basamak_toplami+=int(a)
#     else:
#         if i%basamak_toplami==0:
#             harshad_niven_sayı_listesi+=str(i)+" "
# print(harshad_niven_sayı_listesi,"Sayıları,",baslangıc,"ve",bitis,"Sayıları arasındaki Harshad Niven Sayılarıdır.")


# baslangıc=int(input("10'dan büyük bir başlangıç değeri belirleyiniz: "))
# bitis=int(input("Bir bitiş değeri belirleyiniz: "))
# ters_cift_asal_sayi_listesi=""
# for i in range(baslangıc,bitis):
#     ters_asal=""
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         for k in str(i):
#             ters_asal=k+ters_asal
#         else:
#             for b in range(2,int(ters_asal)):
#                 if int(ters_asal)%b==0:
#                     break
#             else:
#                 print(i,"ve",ters_asal,"Sayıları, Ters Çift Asal Sayılardır. ")
                

# baslangıc=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# print("-"*30)
# for i in range(baslangıc,bitis+1):
#     adet=0
#     ilkyari=""
#     ikinciyari=""
#     sayinin_karesi=i**2
#     adet2=0
#     for basamak in str(sayinin_karesi):
#         adet+=1
#     basamaklarin_yarisi=adet//2
#     if basamaklarin_yarisi!=adet/2:
#         continue
#     for basamak in str(sayinin_karesi):
#         adet2+=1
#         if adet2<=basamaklarin_yarisi:
#             ilkyari+=str(basamak)
#         else:
#             ikinciyari+=str(basamak)
#     if int(ilkyari)+int(ikinciyari)==i:
#         print(sayinin_karesi,"Sayısı",i,"Sayısının karesidir.")
#         print(ilkyari,"+",ikinciyari,"=",i)
#         print(i,"Sayısı Carpet Sayısıdır.")
#         print("-"*30)


# baslangıc=int(input("Bir başlangıç değeri belirleyiniz: "))
# bitis=int(input("Bir bitis değeri belirleyiniz: "))
# for i in range(baslangıc,bitis):
#     basamak_adet=0
#     basamak_ussu_toplam=0
#     for j in str(i):
#         basamak_adet+=1
#     for k in str(i):
#         basamak_ussu_toplam+=int(k)**basamak_adet
#     if basamak_ussu_toplam==i:
#         print(i,"Sayısı Perfect Digital Invariant (PDI) Sayılarındandır.")


# baslangıc=int(input("Bir başlangıç değeri belirleyiniz: "))
# bitis=int(input("Bir bitis değeri belirleyiniz: "))
# for i in range(baslangıc,bitis+1):
#     tam_bolen_toplamlari=0
#     tam_bolenler=""
#     print("-"*65)
#     for j in range(1,i):
#         if i%j==0:
#             tam_bolen_toplamlari+=j
#             tam_bolenler+=str(j)+" "
#     else:
#         print(tam_bolenler,"Sayıları",i,"Sayısının Tam bölenleridir.")
#         print(tam_bolen_toplamlari,"Sayısı",i,"Sayısın Tam Bölenlerinin Toplamıdır.")
#         if tam_bolen_toplamlari<i:
#             print(i,"Sayısı Eksik Sayıdır.")
#         elif tam_bolen_toplamlari<i:
#             print(i,"Sayısı Mükemmel Sayıdır.")
#         else:
#             print(i,"Sayısı Bol Sayıdır.")


# baslangıc=int(input("Bir başlangıç değeri belirleyiniz: "))
# bitis=int(input("Bir bitis değeri belirleyiniz: "))
# for i in range(baslangıc,bitis+1):
#     sayinin_karesi=i**2
#     adet1=0
#     ters_sayi=""
#     duz_sayi=""
#     en_ters_sayi=""
#     adet2=0
#     for l in str(i):
#         adet1+=1
#     for j in str(sayinin_karesi):
#             ters_sayi=j+ters_sayi
#     for k in ters_sayi:
#         adet2+=1
#         if adet2<=adet1:
#             duz_sayi+=k
#     for m in duz_sayi:
#          en_ters_sayi=m+en_ters_sayi
#     if int(en_ters_sayi)==i:
#         print(sayinin_karesi,"Sayısı",i,"Sayısının Karesidir.")
#         print(i,"Sayısı Automorphic Sayıdır.")


# baslangıc=int(input("Aralığınız İçin Bir Başlangıç Değeri Giriniz: "))
# bitis=int(input("Aralığınız İçin Bir Bitiş Değeri Giriniz: "))
# for i in range(baslangıc, bitis):
#     for j in range(2, i+1):
#         asal_bolen_carpımı = 1
#         asal_bolenler_liste = ""
#         if i % j == 0:
#             asal_bolen_carpımı *= j
#             asal_bolenler_liste += str(j) + " "
#             while i!=asal_bolen_carpımı:
#                     oran = i // asal_bolen_carpımı
#                     for l in range(2, oran + 1):
#                         if oran%l==0:
#                             for m in range(2, l):
#                                 if l % m == 0:
#                                     break
#                             else:
#                                 oran//=l
#                                 asal_bolen_carpımı *= l
#                                 asal_bolenler_liste += str(l) + " "
#             print(asal_bolenler_liste, "Sayıları", i, "Sayısının Asal Çarpanlarıdır")
#             break


# baslangıc = int(input("Aralığınız İçin Bir Başlangıç Değeri Giriniz: "))
# bitis = int(input("Aralığınız İçin Bir Bitiş Değeri Giriniz: "))
# for i in range(baslangıc, bitis + 1):
#     fermat_listesi=""
#     for j in range(2, i + 1):
#         for k in range(2, j):
#             if j % k == 0:
#                 break
#         else:
#             if (i ** j - i) % j == 0:
#                 if str(j) not in  fermat_listesi:
#                     fermat_listesi+=str(j)+" "   
# print(fermat_listesi, "Sayısıları Fermat’ın Küçük Teoremine Uyar...")


# terim = int(input("Sınırdaki Terim Sayısını Giriniz: "))
# a,b,c=0,0,1
# tribonacci_dizisi=""
# for i in range(terim):
#     a,b,c=b,c,a+c+b
#     tribonacci_dizisi+=str(c)+" "    
# print(tribonacci_dizisi,"Sayıları Tribonacci Dizisinin",terim,".Terime kadar olan dizisidir.")


# sayi=input("3 Basamaklı Bir Tamsayı Değeri Giriniz: ")
# a,b,c="","",""
# for i in sayi:
#     if a=="":
#         a=int(i)
#     elif b=="":
#         b=int(i)
#     else:
#         c=int(i)
# keith_sayıları=""
# while c!=int(sayi):
#     a,b,c=b,c,a+c+b
#     keith_sayıları+=str(c)+" " 
#     if c>int(sayi):
#         break
# print(keith_sayıları,"Sayıları",sayi,"Sayısının Keith Sayısına göre dizisidir.")   
# if c==int(sayi):
#     print(sayi,"Sayısının Keith Sayısıdır.")
# else:
#     print(sayi,"Sayısının Keith Sayısı değildir.")
            

# baslangıc = int(input("Aralığınız İçin Bir Başlangıç Değeri Giriniz: "))
# bitis = int(input("Aralığınız İçin Bir Bitiş Değeri Giriniz: "))
# for i in range(baslangıc, bitis + 1):
#     sayinin_karesi=i**2
#     sayinin_karesinin_tersi=""
#     for j in str(sayinin_karesi):
#         sayinin_karesinin_tersi=j+sayinin_karesinin_tersi
#     if sayinin_karesinin_tersi==str(sayinin_karesi):
#         print(sayinin_karesi,"Sayısı,",i,"Sayısının Karesidir.")
#         print(i,"Sayısı Palindromik Kare Sayısıdır.")


# baslangıc = int(input("Aralığınız İçin Bir Başlangıç Değeri Giriniz: "))
# bitis = int(input("Aralığınız İçin Bir Bitiş Değeri Giriniz: "))
# semiprime_sayilari=""
# for i in range(baslangıc,bitis+1):
#     for a in range(2,i):
#         if i%a==0:
#             break
#     else:
#         for j in range(2,i+1):
#             for b in range(2,j):
#                 if j%b==0:
#                     break
#             else:
#                 asal_carpim=i*j
#                 if str(asal_carpim) not in semiprime_sayilari:
#                     semiprime_sayilari+=str(asal_carpim)+" "
#                     print(i,"x",j,"=",asal_carpim)
# print(semiprime_sayilari,"Sayıları Semiprime Sayılarıdır.")


# kontrol_sayisi=int(input("Kontrol edeceğiniz tam sayıyı giriniz: "))
# asal_bolen_cifti=""
# asal_carpan=1
# adet=0
# for i in range(2,kontrol_sayisi+1):
#     if kontrol_sayisi%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:   
#             asal_bolen_cifti+=str(i)+" "
#             asal_carpan*=i
#             adet+=1
#         if adet==2:
#             break
# if asal_carpan==kontrol_sayisi:
#     print(kontrol_sayisi,"Sayısı, Semiprime Sayısıdır. ")
# else:
#     print(kontrol_sayisi,"Sayısı, Semiprime Sayısı değildir... ")



# baslangıc = int(input("Aralığınız İçin Bir Başlangıç Değeri Giriniz: "))
# bitis = int(input("Aralığınız İçin Bir Bitiş Değeri Giriniz: "))
# for i in range(baslangıc, bitis + 1):
#     basamak_kupu_toplami=0
#     for a in str(i):
#         basamak_kupu_toplami+=(int(a)**3)
#     if basamak_kupu_toplami==i:
#         print(i,"Sayısı, Küpsel Sayısıdır.")



# baslangıc = int(input("Aralığınız İçin Bir Başlangıç Değeri Giriniz: "))
# bitis = int(input("Aralığınız İçin Bir Bitiş Değeri Giriniz: "))
# for i in range(baslangıc, bitis + 1):
#     basamak_faktoriyeli_toplami=0
#     for a in str(i):
#         basamak_faktoriyeli_=1
#         for j in range(1,int(a)+1):
#             basamak_faktoriyeli_*=j
#         basamak_faktoriyeli_toplami+=basamak_faktoriyeli_
#     if basamak_faktoriyeli_toplami==i:
#         print(i,"Sayısı Faktorion Sayısıdır.")


# sayi=1729
# adet=0
# for i in range(1,sayi+1):
#     for j in range(1,i+1):
#         if sayi==i**3+j**3:
#             print(i**3,"+",j**3,"=",sayi)
#             adet+=1
# else:
#     if adet==2:
#         print(sayi,"Sayısı Ramanujan Hardy Sayılarındandır.")
#     else:
#         print(sayi,"Sayısı Ramanujan Hardy Sayılarından değildir...")


# sayi=1729
# adet=0
# for i in range(1,sayi+1):
#     for j in range(1,i+1):
#         if sayi==i**3+j**3:
#             print(i**3,"+",j**3,"=",sayi)
#             adet+=1
# else:
#     if adet==2:
#         print(sayi,"Sayısı Ramanujan Hardy Sayılarındandır.")
#     else:
#         print(sayi,"Sayısı Ramanujan Hardy Sayılarından değildir...")


# bitis = int(input("Aralığınız İçin Bir Bitiş Değeri Giriniz: "))
# for i in range(1, bitis+1):
#     basamak_adedi=0
#     basamak_ussu_basamak_adedi_toplami=0
#     for k in str(i):
#         basamak_adedi+=1
#     for l in str(i):
#         basamak_ussu_basamak_adedi_toplami+=int(l)**basamak_adedi
#     if basamak_ussu_basamak_adedi_toplami==i:
#         print(i,"Sayısı Armstrong Dizisinin Elemanıdır.")


# n=int(input("n: "))
# cullen_sayi_listesi=""
# for i in range(1,n+1):
#     z=i*2**i+1
#     cullen_sayi_listesi+=str(z)+","
# print(cullen_sayi_listesi,"Sayıları Cullen Dizisinin Elemanlarıdır.")


# bitis=int(input("Bir maksimum değer giriniz: "))
# for i in range(1,bitis+1):
#     for j in range(1,i+1):
#         a=j
#         for k in range(1,j+1):
#             b=k
#             if a**2+b**2==i**2:
#                 print("a: ",b,"b: ",a,"c: ",i,"Sayıları Pisagor Üçlüleridir...")


# bitis=int(input("Bir maksimum değer giriniz: "))
# for i in range(1,bitis+1):
#     for k in range(1,bitis+1):
#         j=i
#         ardısık_karelerin_toplami=0   
#         ardısık_kareler_listesi=""
#         ardısık_sayi_adedi=0
#         while ardısık_karelerin_toplami<k:
#             ardısık_karelerin_toplami+=j**2
#             ardısık_kareler_listesi+=str(j)+" "
#             ardısık_sayi_adedi+=1
#             j+=1
#             if ardısık_karelerin_toplami == k and ardısık_sayi_adedi>2:
#                 print(ardısık_kareler_listesi,"Ardışık Sayılarının Karelerin Toplamı",ardısık_karelerin_toplami,"Sayısına Eşittir.")
#                 break
        
