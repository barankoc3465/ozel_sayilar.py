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




# bitis=int(input("Bir maksimum değer giriniz: "))
# for i in range(1,bitis):
#     rakamlarin_karesi_toplami=0
#     for j in str(i):
#         rakamlarin_karesi_toplami+=int(j)**2
#         adet=0
#         while rakamlarin_karesi_toplami!=1:
#             rakamlarin_karesi_toplami=0
#             for k in str(rakamlarin_karesi_toplami):
#                 rakamlarin_karesi_toplami+=int(j)**2
#                 adet+=1
#             if adet==15:
#                 break
#         else:
#             print(i, "Sayısı Happy Numbers (Mutlu Sayılar) Familyasındandır.")
    



# bitis=int(input("Bir maksimum değer giriniz: "))
# for i in range(1,bitis):
#     a=i
#     for j in range(1,bitis):
#         b=j
#         for k in range(1,bitis):
#             c=k
#             harmonik_ortalama_sayilari=3/((b*c+a*c+b*a)/(a*b*c))
#             if harmonik_ortalama_sayilari==int(harmonik_ortalama_sayilari):
#                 print(a,b,c,sep=", ")




# baslangıc=int(input("Bir Başlangıç değeri giriniz: "))
# bitis=int(input("Bir Bitiş değeri giriniz: "))
# for i in range(baslangıc,bitis+1):
#     asal_carpan_listesi=""
#     asal_carpanlar=1
#     for j in range(2,i):
#         if i%j==0:
#             while asal_carpanlar!=i:
#                 oran=i//asal_carpanlar
#                 for m in range(2,oran+1):
#                     if oran%m==0:
#                         for k in range(2,m):
#                             if m%k==0:
#                                 break
#                         else:
#                             asal_carpan_listesi+=str(m)+" "
#                             asal_carpanlar*=m
#             else:
#                 print(asal_carpan_listesi,"Sayıları",i,"Sayısının Asal Çarpanlarıdır.")
#                 break




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(baslangic,bitis):
#     oran=i
#     while oran!=1 and oran%10!=0:
#         basamak_rakamlarinin_toplami=0
#         for j in str(oran):
#             basamak_rakamlarinin_toplami+=int(j)
#         if i%basamak_rakamlarinin_toplami==0:
#             oran//=basamak_rakamlarinin_toplami
#         else:
#             break
#         if oran==1:
#             print(i,"Sayısı Harshad Zincirini Oluşturur...")
            



# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(baslangic,bitis+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         for k in range(2,i+2):
#             if (i + 2) % k == 0:
#                 break   
#         else:
#             ters_sayi1=""
#             ters_sayi2=""
#             for l in str(i):
#                 ters_sayi1=l+ters_sayi1
#             for m in str(i+2):
#                 ters_sayi2=m+ters_sayi2
#             if int(ters_sayi2)==i+2 or int(ters_sayi1)==i:
#                 print(i,"ve",i+2,"Sayıları Polindromik İkiz Asal Sayılardır.")
#             else:
#                 print(i,"ve",i+2,"Sayıları İkiz Asal Sayılardır.")




# tekrar çöz 
# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# yaraticisi_olan_sayilar_listesi=""
# for i in range(baslangic,bitis+1):
#     basamak_toplami=0
#     for j in str(i):
#         basamak_toplami+=int(j)
#     else:
#         yaraticisi_olan_sayilar=basamak_toplami+i
#         if str(yaraticisi_olan_sayilar) not in yaraticisi_olan_sayilar_listesi:
#             yaraticisi_olan_sayilar_listesi+=str(yaraticisi_olan_sayilar)+" "
# for k in range(baslangic,bitis+1):
#     if str(k) not in yaraticisi_olan_sayilar_listesi:
#         print(k,"sayısı Kapalı bir sayıdır.")




# n=int(input("Bir tam sayı değeri giriniz: "))
# adet=0
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("K",end="")
#             adet+=1
#         else:
#             print("",end=" ")
#     print()
# print(adet,"sayısı kapsanan kare sayısıdır.")




# bitis=int(input("Bir bitiş değeri giriniz: "))
# print("-"*50)
# while True:
#     for j in range(2,bitis):
#         for k in range(2,bitis):
#             leyland_sayisi=j**k+k**j
#             if type(leyland_sayisi)==int and leyland_sayisi<bitis and j>k:
#                 print(j,"ve",k,"sayıları",leyland_sayisi,"Sayısının asal çarpanlarıdır.")
#                 print(leyland_sayisi,"Sayısı Leyland Sayılarındandır.")
#                 print("-"*50)
#     else:
#         break




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(baslangic,bitis):
#     ters_sayi=""
#     for j in str(i):
#         ters_sayi=j+ters_sayi
#     else:
#         ters_duz_carpim=int(ters_sayi)*i
#         ters_duz_carpim_tersi=""
#         for k in str(ters_duz_carpim):
#             ters_duz_carpim_tersi=k+ters_duz_carpim_tersi
#         else:
#             if int(ters_duz_carpim_tersi)==ters_duz_carpim:
#                 print(i,"ve",ters_sayi,"sayılarının çarpımı olan",ters_duz_carpim,"sayısı polindrom")




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(baslangic,bitis):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         ters_asal=""
#         for k in str(i):
#             ters_asal=k+ters_asal
#         else:
#             for l in range(2,int(ters_asal)):
#                 if int(ters_asal)%l==0:
#                     break
#             else:
#                 print(i,"sayısı mükemmel bir asal sayıdır.")




# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(bitis+1):
#     fermat_sayisi=(4)**i+1
#     print(fermat_sayisi,"sayısı bir fermat sayısıdır.")




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# print("-"*50)
# for i in range(baslangic,bitis):
#     basamak_toplami_dongusel=i
#     while True:
#         basamak_toplami=0
#         dijital_kok_zinciri=""
#         dongu_seferi=0
#         for j in str(basamak_toplami_dongusel):
#             basamak_toplami+=int(j)
#             dijital_kok_zinciri+=j+" "
#             dongu_seferi+=1
#         else:
#             if len(str(basamak_toplami))==1:
#                 print(basamak_toplami,i,"sayısının Dijital Köküdür.")
#                 break
#             else:
#                 print(basamak_toplami,"sayısı,",dongu_seferi,".zincirde",dijital_kok_zinciri,"sayılarının toplamıdır.")
#                 basamak_toplami_dongusel=basamak_toplami
#     print("-"*50)




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# print("-"*50)
# for i in range(baslangic,bitis):
#     adet=0
#     asal_carpanlar=""
#     for j in range(2,i):
#         if i%j==0:
#             for k in range(2,j):
#                 if j%k==0:
#                     break
#             else:
#                 adet+=1
#                 asal_carpanlar+=str(j)+" "
#     else:
#         if adet==2:
#             print(asal_carpanlar)
#             print(i,"sayısı Yarı Asal sayıdır.")
#             print("-"*50)




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(baslangic,bitis):
#     sayinin_karesi=i**2
#     if len(str(sayinin_karesi))>=2:
#         sayinin_karesinin_ilk_yari=""
#         sayinin_karesinin_ikinci_yari=""
#         basamak_sayisi=0
#         basamak_sayisi_ikinci_dongu=0
#         for j in str(sayinin_karesi):
#             basamak_sayisi+=1
#         for k in str(sayinin_karesi):
#             basamak_sayisi_ikinci_dongu+=1
#             if basamak_sayisi_ikinci_dongu<=basamak_sayisi/2:
#                 sayinin_karesinin_ilk_yari+=str(k)
#             else:
#                 sayinin_karesinin_ikinci_yari+=str(k)
#         else:
#             ilk_iki_toplamı=int(sayinin_karesinin_ilk_yari)+int(sayinin_karesinin_ikinci_yari)
#             if ilk_iki_toplamı==i:
#                 print(i,"sayısı Kaprekar sayılarındandır.")
#     else:
#         continue




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# print("Harshad (Niven) Zincirleri")
# for i in range(baslangic,bitis):
#     adet=0
#     a=i
#     while i!=10 and i!=1:
#         rakamlar_toplami=0
#         adet+=1
#         for j in str(i):
#             rakamlar_toplami+=int(j)
#         else:
#             if i%rakamlar_toplami==0:
#                 i=i//rakamlar_toplami
#             else:
#                 break
#     else:
#         if a!=10 and a!=1:
#             print(a,"sayısı",adet,"kez döndükten sonra 1'e eşitlenir.")




# baslangic=int(input("Bir başlangıç değeri giriniz: "))
# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(baslangic,bitis):
#     basamak_adedi=0
#     basamak_ussu=0
#     for j in str(i):
#         basamak_adedi+=1
#     else:
#         for k in str(i):
#             basamak_ussu+=int(k)**basamak_adedi
#         else:
#             if basamak_ussu==i:
#                 print(i,"sayısı Narcissistic Sayılar (Kendi Gücü Sayılar) dandır.")




# bitis=int(input("Bir bitiş değeri giriniz: "))
# for i in range(1,bitis):
#     for j in range(i+1,bitis):
#         dorduncu_kuvvet=i**4+j**4
#         if dorduncu_kuvvet<bitis:
#             print(j,"ve",i,"sayılarının dördüncü kuvvetinin toplamı:")
#             print(dorduncu_kuvvet,"sayısı dördün gücü ile oluşan bir sayıdır.")
        



# sayi=int(input("Bir sayı giriniz: "))
# for i in range(1,(sayi//3)*2+1):
#     ardisik_toplam=0
#     ardisik_sayi_listesi=""
#     for j in range(i,0,-1):
#         ardisik_toplam+=j
#         ardisik_sayi_listesi+=str(j)+" "
#         if ardisik_toplam==sayi:
#             print(sayi,"sayısı",ardisik_sayi_listesi,"sayılarının toplamına eşittir.")




# bitis=int(input("aralığınızın bitiş değerini giriniz: "))
# for i in range(1,bitis):
#     for j in range(1,(i//3)*2+1):
#         ardisik_toplam=0
#         ardisik_sayi_listesi=""
#         for k in range(j,0,-1):
#             ardisik_toplam+=k
#             ardisik_sayi_listesi+=str(k)+" "
#             if ardisik_toplam==i:
#                 print(i,"sayısı",ardisik_sayi_listesi,"sayılarının toplamına eşittir.")
#                 print("-"*70)
            



# for i in range(1,1000):
#     a=i
#     b=i
#     while i!=1 and i%10!=0:
#         rakamlar_toplami=0
#         for j in str(i):
#             rakamlar_toplami+=int(j)
#         else:
#             if i%rakamlar_toplami==0:
#                 i//=rakamlar_toplami
#                 if i==1:
#                     rakamlarin_bir_artimi=""
#                     for j in str(a):
#                         for k in str(int(j)+1):
#                             rakamlarin_bir_artimi+=k
#                     a=int(rakamlarin_bir_artimi)
#                     while a!=1 and a%10!=0:
#                         rakamlar_toplami=0
#                         for j in str(a):
#                                 rakamlar_toplami+=int(j)
#                         else:
#                             if a%rakamlar_toplami==0:
#                                 a//=rakamlar_toplami
#                                 if a==1:
#                                     print(b,"sayısı alternatif harshad niven sayısıdır.") 
#                             else:
#                                 break                   
#             else:
#                 break   




# sayi=int(input("bir sayı giriniz: "))
# asal_sayi_listesi=""
# for i in range(1,sayi+1):
#     for j in range(2,i):
#         if i%j ==0 :
#             break
#     else:
#         asal_sayi_listesi+=str(i)+" "
# for i in range(1,sayi):
#     basamak_toplami=0
#     for j in str(i):
#         basamak_toplami+=int(j)
#     a=i
#     asal_bolenler_basamak_toplami=0
#     asal_bolenler="-"
#     while i!=1:  
#         for k in range(2,i+1):
#             if i%k==0:
#                 for l in range(2,k):
#                     if k%l==0:
#                         break
#                 else:
#                     for m in str(k):
#                         asal_bolenler_basamak_toplami+=int(m)
#                         asal_bolenler+=m+""
#                     else:
#                         i//=k   
#                         asal_bolenler+="-"
#                         break
#         else:
#             break
#     if str(a) not in asal_sayi_listesi:
#         if i==1 and asal_bolenler_basamak_toplami==basamak_toplami:
#             print(a,"sayısı Smith sayısıdır.")
#             print("asal bölenler: ",asal_bolenler)
#             print("-"*50)




# bitis=int(input("Bir sayı giriniz: "))
# for i in range(1,bitis):
#     bolenler_toplami=0
#     bolenler_sayisi=""
#     for j in range(1,i+1):
#         if i%j==0:
#             bolenler_toplami+=j
#             bolenler_sayisi+=str(j)+" "
#     else:
#         if 2*i==bolenler_toplami:
#             print(bolenler_sayisi,"sayıları",i,"sayısının bölenleridir.")
            



# a,b=0,1
# n=int(input("n: "))
# for i in range(n):
#     a,b=b,b+a
#     print(b)




# baslangıc=int(input("bir başlangıç değeri giriniz: "))
# bitis=int(input("bir bitiş değeri giriniz: "))
# fraktal_ucgen_sayilari=[]
# for i in range(baslangıc,bitis+1):
#     fraktal_ucgen_sayisi=i*(i+1)/2
#     fraktal_ucgen_sayilari.append(int(fraktal_ucgen_sayisi))
# else:
#     print(fraktal_ucgen_sayilari)




# baslangıc=int(input("bir başlangıç değeri giriniz: "))
# bitis=int(input("bir bitiş değeri giriniz: "))
# dijital_sarmal_problemi=[]
# for i in range(baslangıc,bitis):
#     if len(str(i))%2!=0:
#         continue
#     else:
#         sayinin_yarisi=""
#         sayinin_yarisinin_tersi=""
#         sayinin_yarisinin_tersinin_tersi=""
#         adet=0
#         for j in str(i):
#             adet+=1
#             if adet<=len(str(i))/2:
#                 sayinin_yarisi+=j
#             else:
#                 sayinin_yarisinin_tersi+=j
#         else:
#             for k in str(sayinin_yarisinin_tersi):
#                 sayinin_yarisinin_tersinin_tersi=k+sayinin_yarisinin_tersinin_tersi
#             else:
#                 if sayinin_yarisinin_tersinin_tersi==sayinin_yarisi:
#                     dijital_sarmal_problemi.append(i)
# else:
#     print(dijital_sarmal_problemi)




# bitis=int(input("Bir bitiş değeri giriniz: "))
# repetitif_sayilar=[]
# for i in range(1,bitis):
#     for j in str(i):
#         ilk_rakam=int(j)
#         break
#     for k in str(i):
#         if ilk_rakam!=int(k):
#             break
#     else:
#         repetitif_sayilar.append(i)
# else:
#     print("""Repetitif Sayılar:
# """,repetitif_sayilar,sep="")




# bitis=int(input("Bir bitiş değeri giriniz: "))
# hiperbolik_sayilar=[]
# for i in range(1,bitis):
#     hiperbolik_sayi_denemesi=i**2+1
#     for j in range(2,hiperbolik_sayi_denemesi):
#         if hiperbolik_sayi_denemesi%j==0:
#             break
#     else:
#         hiperbolik_sayilar.append(hiperbolik_sayi_denemesi)
# else:
#     print(hiperbolik_sayilar)




# bitis=int(input("Bir bitiş değeri giriniz: "))
# hiperbolik_sayilar=[]
# for i in range(2,bitis):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if (i-1)**0.5==int((i-1)**0.5):
#           hiperbolik_sayilar.append(i)
# else:
#     print(hiperbolik_sayilar)




# bitis=int(input("bir bitiş değeri giriniz: "))
# ciftler_icindeki_mukemmel_sayilar=[]
# for c in range(1,bitis):
#     if c%2==0:
#         for b in range(1,c):
#             a=c//b
#             if b+a==c and a==c/b:
#                 ciftler_icindeki_mukemmel_sayilar.append(c)
# else:
#     print(ciftler_icindeki_mukemmel_sayilar)




# bitis=int(input("bir bitiş değeri giriniz: "))
# duzensiz_sayilar=[]
# for i in range(1,bitis+1):
#     pozitif_carpanlar_carpimi=1
#     pozitif_carpanlar_toplami=0
#     for j in range(1,i+1):
#         if i%j==0:
#             pozitif_carpanlar_carpimi*=j
#             pozitif_carpanlar_toplami+=j
#     else:
#         if pozitif_carpanlar_toplami>pozitif_carpanlar_carpimi:
#             duzensiz_sayilar.append(i)
# else:
#     print(duzensiz_sayilar)# asal sayıların başka bir tanımı




# bitis=int(input("bir bitiş değeri giriniz: "))
# ardisik_carpanlar_listesi=[]
# ardisik_carpanlar=1
# a=1
# while ardisik_carpanlar<bitis :
#     ardisik_carpanlar=a*(a+1)
#     ardisik_carpanlar_listesi.append(ardisik_carpanlar)
#     a+=1
# print(ardisik_carpanlar_listesi)




# baslangıc=int(input("bir başlangıç değeri giriniz: "))
# bitis=int(input("bir bitiş değeri giriniz: "))
# ardisik_carpanlar_listesi=[]
# a=False
# for i in range(baslangıc,bitis+1):
#     for j in range(1,i):
#         if i%j==0:
#             if j*(i//j+1)==i:
#                 b=j
#                 a=True
#                 break
#     if a==True:
#         break
# ardisik_carpanlar=1
# while ardisik_carpanlar<bitis:
#     ardisik_carpanlar=b*(b+1)
#     ardisik_carpanlar_listesi.append(ardisik_carpanlar)
#     b+=1
# print(ardisik_carpanlar_listesi)




# bitis=int(input("bir bitiş değeri giriniz: "))
# for i in range(1,bitis):
#     polindromik_carpanlar=[]
#     for j in range(1,i+1):
#         if j>10 and i%j==0:
#             ters_carpan=""
#             for k in str(j):
#                 ters_carpan=k+ters_carpan
#             else:
#                 if int(ters_carpan)==j:
#                     polindromik_carpanlar.append(j)
#     else:
#         if polindromik_carpanlar:
#             print(i,"sayısının polindromik çarpanları: ",polindromik_carpanlar)




# a1=int(input("bir asal sayı tuşlayınız: "))
# k=int(input("bir artış miktarı tuşlayınız: "))
# n=int(input("bir terim sayısı tuşlayınız: "))
# asal_dizisi=[]
# for m in range(n):
#     for i in range(n):
#         a1+=k
#         for j in range(2,a1):
#             if a1%j==0:
#                 break
#         else:
#             asal_dizisi.append(a1)  
#             break    
# else:
#     print(asal_dizisi)




# uc_bes_toplam=0
# for i in range(1,1001):
#     if i%3==0 or i%5==0:
#         uc_bes_toplam+=i
# print(uc_bes_toplam)




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




# bitis=int(input("bir bitiş değeri giriniz: "))
# for i in range(1,bitis):
#     basamak_toplami=0
#     asal_carpanlar_basamak_toplami=0
#     asal_carpanlar=[]
#     for j in str(i):
#         basamak_toplami+=int(j)
#     else:
#         for k in range(2,int(i)):
#             if i%k==0:
#                 for l in range(2,k):
#                     if k%l==0:
#                         break
#                 else:
#                     asal_carpanlar.append(k)
#                     for m in str(k):
#                         asal_carpanlar_basamak_toplami+=int(m)
#         else:
#             if asal_carpanlar_basamak_toplami==basamak_toplami:
#                 print(i,"sayısı Smith sayısıdır. Asal çarpanları: ",asal_carpanlar)




# karesel_toplam_sayilari=[]
# i=1
# bitis=int(input("bir bitiş değeri giriniz: "))
# while i!=bitis:
#     i+=1
#     kare_konrolu=0
#     for j in str(i):
#         kare_konrolu+=int(j)**2
#     else:
#         if kare_konrolu**0.5==int(kare_konrolu**0.5):
#             karesel_toplam_sayilari.append(i)
# print(karesel_toplam_sayilari)




# asal_cift_listesi=[]
# for i in range(1000,1255):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         for k in range(2,i-2):
#             if (i-2)%k==0:
#                 break
#         else:
#             asal_cift=i,i-2
#             asal_cift_listesi.append(asal_cift)
# else:
#     print(asal_cift_listesi)
    



# bitis=int(input("bir bitiş değeri giriniz: "))
# i=0
# armstrong_sayilari_listesi=[]
# while i<bitis:
#     i+=1
#     armstrong_kup_toplami=0
#     for k in str(i):
#         armstrong_kup_toplami+=int(k)**3
#     else:
#         if armstrong_kup_toplami==i:
#             armstrong_sayilari_listesi.append(i)
#             print(i)
# print(armstrong_sayilari_listesi)




# faktoriyel=1
# i=0
# bitis=int(input("bir bitiş değeri giriniz: "))
# while i<bitis:
#     i+=1
#     sifir_adedi=0
#     faktoriyel*=i
#     for k in str(faktoriyel):
#         if str(0) in k:
#             sifir_adedi+=1
#     else:
#         print(i,"Sayısının Faktöriyelinde",sifir_adedi,"adet 0 vardır.")




# z=1
# n=int(input("n: "))
# ussu=1
# faktoriyel=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         ussu=ussu*i
#     for j in range(1,i+1):
#         faktoriyel=faktoriyel*j
#     z=z*(ussu/faktoriyel)
# print(z)




# sihirli_sayi=[]
# for i in range(1,10000):
#     rakamlar_toplami=0
#     rakamlar_carpimi=1
#     for j in str(i):
#         rakamlar_toplami+=int(j)
#         rakamlar_carpimi*=int(j)
#     else:
#         if rakamlar_carpimi+rakamlar_toplami==i:
#             sihirli_sayi.append(i)
# else:
#     print(sihirli_sayi)




# baslangic=int(input("bir başlangıç değeri giriniz: "))
# bitis=int(input("bir bitiş değeri giriniz: "))
# alternatif_basamak_sayilari_listesi=[]
# for i in range(baslangic,bitis):
#     adet=0
#     tek_basamak_toplami=0
#     cift_basamak_toplami=0
#     ters_sayi=""
#     for j in str(i):  
#         ters_sayi=j+ters_sayi
#     for j in str(ters_sayi):
#         adet+=1
#         if adet%2==1:
#             tek_basamak_toplami+=int(j)
#         else:
#             cift_basamak_toplami+=int(j)
#     else:
#         if tek_basamak_toplami==cift_basamak_toplami:
#             alternatif_basamak_sayilari_listesi.append(i)
# else:
#     print(alternatif_basamak_sayilari_listesi)




# ucgen_ve_kare_sayilar_listesi=[]
# for i in range(1,100):
#     for j in range(1,i+1):
#         kare_sayi=j*j
#         for k in range(1,i+1):
#             ucgen_sayi=k*(k+1)//2
#         if ucgen_sayi==kare_sayi:
#             ucgen_ve_kare_sayilar_listesi.append(ucgen_sayi)
# else:
#     print(ucgen_ve_kare_sayilar_listesi)




# a,b=1,1
# bitis=int(input("bir bitis değeri giriniz: "))
# fibonacci_asal_sayilar_listesi=[]
# while b<bitis:
#     a,b=b,a+b
#     for j in range(2,b):
#         if b%j==0:
#             break
#     else:
#         fibonacci_asal_sayilar_listesi.append(b)
#         print(b)
# else:
#     print(fibonacci_asal_sayilar_listesi)



# bitis=int(input("bir bitiş değeri giriniz: "))
# harshad_niven_sayilari_listesi=[]
# for i in range(1,bitis):
#     rakamlar_toplami=0
#     for j in str(i):    
#         rakamlar_toplami+=int(j)
#     else:
#         if i%rakamlar_toplami==0:
#             harshad_niven_sayilari_listesi.append(i) 
# else:
#     print(harshad_niven_sayilari_listesi)



# bitis=int(input("bir bitiş değeri giriniz: "))
# for i in range(1,bitis):
#     a=i
#     while True:
#         rakamlar_carpim=1
#         for j in str(i):
#             rakamlar_carpim*=int(j)
#         else:
#             if len(str(rakamlar_carpim))==1:
#                 print(a,rakamlar_carpim)
#                 break
#             else:
#                 i=rakamlar_carpim




# a,b=0,1
# bitis=int(input("bir bitiş değeri giriniz: "))
# fibonacci_sayilari_listesi=[]
# altin_cift_sayilar_listesi=[]
# while b<bitis:
#     a,b=b,a+b
#     fibonacci_sayilari_listesi.append(b)
# for i in range(1,bitis):
#     for j in range(1,i):
#         if (i+j)**0.5==int((i+j)**0.5):
#             if i*j in fibonacci_sayilari_listesi:
#                 altin_cift_sayilar=i,j
#                 altin_cift_sayilar_listesi.append(altin_cift_sayilar)
# else:
#     print(altin_cift_sayilar_listesi)




# i=0
# while i<1000:
#     i+=1
#     a=i
#     ciftlik_adimi_sayisi=0
#     while a%2!=0:
#         ters_sayi=""
#         ciftlik_adimi_sayisi+=1 
#         for j in str(a):
#             ters_sayi=j+ters_sayi
#         else:
#             a+=int(ters_sayi)
#     if ciftlik_adimi_sayisi>0:
#         print(i,ciftlik_adimi_sayisi)



# i=0
# bitis=int(input("bir bitiş değeri giriniz: "))
# ters_toplam_kare_listesi=[]
# while i<bitis:
#     i+=1
#     ters_i=""
#     for j in str(i):
#         ters_i=j+ters_i
#     else:
#         if (i+int(ters_i))**0.5==int((i+int(ters_i))**0.5):
#             ters_toplam_kare_listesi.append(i)
# print(ters_toplam_kare_listesi)




# sayi1=int(input("1.sayınızı giriniz: "))
# sayi2=int(input("2.sayınızı giriniz: "))
# a,b=0,1
# fibonacci_cifti_listesi=[]
# while b<sayi1+sayi2:
#     a,b=b,b+a
#     fibonacci_cifti=a,b
#     fibonacci_cifti_listesi.append(fibonacci_cifti)
# kontrol_listesi=sayi1,sayi2
# if kontrol_listesi in fibonacci_cifti_listesi:
#     print(kontrol_listesi,"sayı çifti 2 ardışık fibonacci sayısıdır.")
# else:
#     print("değildir.")




# bitis=int(input("bir sayı giriniz: "))
# bolunebilen_ters_sayi_listesi=[]
# for i in range(1,bitis):
#     ters_sayi=""
#     for j in str(i):
#         ters_sayi=j+ters_sayi
#     else:
#         if i%int(ters_sayi)==0:
#             bolunebilen_ters_sayi_listesi.append(i)
# else:
#     print(bolunebilen_ters_sayi_listesi)
    


# bes_ogrencinin_toplam_notu=0
# for i in range(1,6):
#     toplam_not=0
#     for j in range(1,4):
#         org_not=int(input(str(i)+". Öğrencinin "+str(j)+". Notu: "))
#         toplam_not+=org_not
#     ortalama_notu=toplam_not/3
#     print(i,".ögrencinin ortalaması :",ortalama_notu)
#     bes_ogrencinin_toplam_notu+=ortalama_notu
# bes_ogrencinin_ortalaması=bes_ogrencinin_toplam_notu/5
# print("5 öğrencinin ortalaması: ",bes_ogrencinin_ortalaması)




# lychrel_sayilari_listesi = []
# for i in range(1, 10000):
#     a = i
#     tekrar_sayisi = 0
#     while tekrar_sayisi < 50:
#         ters_sayi = ""
#         for j in str(i):
#             ters_sayi = j + ters_sayi
#         ters_toplam_sayisi = ""
#         toplam = i + int(ters_sayi)
#         for k in str(toplam):
#             ters_toplam_sayisi = k + ters_toplam_sayisi
#         ters_toplam_sayisinin_tersi = ""
#         for l in str(ters_toplam_sayisi):
#             ters_toplam_sayisinin_tersi = l + ters_toplam_sayisinin_tersi
#         if int(ters_toplam_sayisinin_tersi) == int(ters_toplam_sayisi):
#             break
#         else:
#             i = toplam
#             tekrar_sayisi += 1
#             if tekrar_sayisi == 50:
#                 lychrel_sayilari_listesi.append(a)
#                 break
# print(lychrel_sayilari_listesi)
# print("""55.Soru'nun cevabı:
# """, len(lychrel_sayilari_listesi), sep="")




# bitis=int(input("bir bitiş değeri giriniz:"))
# altin_dikdortgen_sayilari=[]
# for a in range(1,bitis+1):
#     if a**0.5!=int(a**0.5):
#         b=a*1.618
#         dikdortgen_kenarlari=a,b
#         altin_dikdortgen_sayilari.append(dikdortgen_kenarlari)
# else:
#     print(altin_dikdortgen_sayilari)




# bitis=int(input("bir bitiş değeri giriniz: "))
# kendi_kendine_bolunen_sayilar_listesi=[]
# for i in range(1,bitis):
#     for j in str(i):
#         if j!="0":
#             if i%int(j)==0:
#                 pass
#             else:
#                 break
#         else:
#             break
#     else:
#         kendi_kendine_bolunen_sayilar_listesi.append(i)
# else:
#     print(kendi_kendine_bolunen_sayilar_listesi)



# bitis=int(input("bir bitiş değeri giriniz: "))
# cift_rakam_sayilari=[]
# for i in range(1,bitis):
#     for j in str(i):
#         if int(j)%2!=0:
#             break
#     else:
#         cift_rakam_sayilari.append(i)
# else:
#     print(cift_rakam_sayilari)
        


# bitis=int(input(" bir tam sayı değeri tuşlayınız: "))
# kok_carpan_esit_sayi_listesi=[]
# for i in range(1,bitis):
#     if i**0.5==int(i**0.5):
#         kok_carpanlari_toplami=0
#         for j in range(1,int(i**0.5)+1):
#             if int(i**0.5)%j==0:
#                 kok_carpanlari_toplami+=j
#         else:
#             if kok_carpanlari_toplami==i:
#                 kok_carpan_esit_sayi_listesi.append(i)
# else:
#     print(kok_carpan_esit_sayi_listesi)




# bitis=int(input("bir bitiş değeri giriniz: "))
# mukemmel_cift_listesi=[]
# for i in range(1,bitis):
#     print(i)
#     for j in range(1,i):
#         if (i+j)**0.5==int((i+j)**0.5) and i-j!=1:
#             for k in range(2,i-j):
#                 if (i-j)%k==0:
#                     break
#             else:
#                 mukemmel_cift=j,i
#                 mukemmel_cift_listesi.append(mukemmel_cift)
# else: 
#     print(mukemmel_cift_listesi)




# farkli_rakam_sayilari=[]
# for i in range(1,10000):
#     farkli_rakam_kontrol_listesi=[]
#     farkli_rakam_kontrol_kumesi=set()
#     for j in str(i):
#         farkli_rakam_kontrol_listesi.append(j)
#     else:
#         for j in farkli_rakam_kontrol_listesi:
#             farkli_rakam_kontrol_kumesi.add(j)
#         else:
#             if len(farkli_rakam_kontrol_kumesi)==len(farkli_rakam_kontrol_listesi):
#                 farkli_rakam_sayilari.append(i)
# else:
#     print(farkli_rakam_sayilari)
#     print(len(farkli_rakam_sayilari))




# ters_faktoriyel_sayilari_listesi=[]
# faktoriyel=1
# for i in range(1,5):
#     faktoriyel*=i
#     ters_faktoriyel=""
#     adet=0
#     for j in str(faktoriyel):
#         adet+=1
#         if adet==len(str(faktoriyel)) and int(j)==0:
#             break
#         ters_faktoriyel=j+ters_faktoriyel
#     else:
#         ters_faktoriyel_sayilari_listesi.append(int(ters_faktoriyel))
# else:
#     print(ters_faktoriyel_sayilari_listesi)        





# rakamlari_karesi_toplami_kendise_esit_listesi=[]
# for i in range(1,1000):
#     rakamalar_karesi_toplami=0
#     for j in str(i):
#         rakamalar_karesi_toplami+=int(j)**3
#     else:
#         if rakamalar_karesi_toplami==i:
#             rakamlari_karesi_toplami_kendise_esit_listesi.append(i)
# else:
#     print(rakamlari_karesi_toplami_kendise_esit_listesi)




# a=1
# b=1
# dizi_uzunlugu=0
# fibonacci_listesi=[]
# ters_fibonacci_listesi=[]
# ters_duz_fibonacci_listesi=[]
# while dizi_uzunlugu<1000:
#     ters_fibonacci=""
#     dizi_uzunlugu+=1
#     c=a
#     a=b
#     b=b+c
#     for i in str(a):
#         ters_fibonacci=i+ters_fibonacci
#     else:
#         ters_fibonacci_listesi.append(int(ters_fibonacci))
#         fibonacci_listesi.append(a)
# for i in ters_fibonacci_listesi:
#     if i in fibonacci_listesi:
#         print(i)
#         ters_duz_fibonacci_listesi.append(i)
# else:
#     print(ters_duz_fibonacci_listesi)




# rakam_ciftligi_listesi=[]
# sayi=0
# while sayi<10000:
#     sayi+=1
#     tek_rakam_toplami=0
#     cift_rakam_toplami=0
#     for i in str(sayi):
#         if int(i)%2==0:
#             cift_rakam_toplami+=int(i)
#         else:
#             tek_rakam_toplami+=int(i)
#     else:
#         if cift_rakam_toplami==tek_rakam_toplami:
#             rakam_ciftligi_listesi.append(sayi)
# print(rakam_ciftligi_listesi)
# rakam_ciftligi_listesinin_toplami=0
# for i in rakam_ciftligi_listesi:
#     rakam_ciftligi_listesinin_toplami+=i
# else:
#     print(rakam_ciftligi_listesinin_toplami)




# kara_kup_esit_listesi=[]
# for i in range(1,10000):
#     if (i**3)**(0.5)==int((i**3)**(0.5)):
#         kara_kup_esit_listesi.append(i)
# else:
#     kara_kup_esit_listesinin_toplami=0
#     for i in kara_kup_esit_listesi:
#         kara_kup_esit_listesinin_toplami+=i
#     else:
#         print(kara_kup_esit_listesinin_toplami)




# a=1
# b=1
# fibonacci_listesi=[]
# fibonacci_asali_listesi=[]
# fibonacci_asali_listesinin_toplami=0
# terim_sayisi=0
# while terim_sayisi<30:
#     terim_sayisi+=1
#     c=a
#     a=b
#     b=c+b
#     fibonacci_listesi.append(a)
# for i in fibonacci_listesi:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         fibonacci_asali_listesi.append(i)
# else:
#     for k in fibonacci_asali_listesi:
#         fibonacci_asali_listesinin_toplami+=k
#     else:
#         print("Asal Fibonacci Sayıları: ",fibonacci_asali_listesi)
#         print("Asal Fibonacci Sayılarının Toplamı: ",fibonacci_asali_listesinin_toplami)




# dijital_mukemmel_Sayilar=[]
# for i in range(1,10000):
#     rakamlar_carpimi=1
#     for j in str(i):
#         rakamlar_carpimi*=int(j)
#     else:
#         carpimler_toplami=0
#         for k in range(1,rakamlar_carpimi):
#             if rakamlar_carpimi%k==0:
#                 carpimler_toplami+=k
#         else:
#             if rakamlar_carpimi!=0 and carpimler_toplami==rakamlar_carpimi:
#                 dijital_mukemmel_Sayilar.append(i)
# else:
#     dijital_mukemmel_toplamlari=0
#     for i in dijital_mukemmel_Sayilar:
#         dijital_mukemmel_toplamlari+=i
#     else:
#         print(dijital_mukemmel_Sayilar)
#         print(dijital_mukemmel_toplamlari)




# for i in range(2,100):
#     asal_carpanlar=[]
#     a=i
#     asal_sayi_kontrolu=0
#     while i!=1:
#         for j in range(2,i+1):
#             if i%j==0:
#                 for k in range(2,j):
#                     if j%k==0:
#                         break
#                 else:
#                     asal_sayi_kontrolu+=1
#                     i//=j
#                     asal_carpanlar.append(j)
#     else:
#         if asal_sayi_kontrolu!=1: 
#             asal_carpanlar.sort()
#             print(a,asal_carpanlar)




# yinenlenen_kare_sayilari=[]
# sayi=1
# while sayi<1000:
#     sayi+=1
#     a=sayi
#     dongu_sayisi=0
#     while True:
#         if a**0.5==int(a**0.5):
#             a=int(a**0.5)
#             dongu_sayisi+=1
#             if dongu_sayisi==2:
#                 yinenlenen_kare_sayilari.append(sayi)
#                 break
#         else:
#             break
# print(yinenlenen_kare_sayilari)
# for i in range(1,21):
#     print(i**4)




# cift_ve_rakamalari_asallar=[]
# for i in range(2,100000):
#     if i%2==0:
#         rakam_adedi=0
#         for j in str(i):
#             if int(j)>1:
#                 for k in range(2,int(j)):
#                     if int(j)%k==0:
#                         break
#                 else:
#                     rakam_adedi+=1
#         else:
#             if rakam_adedi==len(str(i)):
#                 cift_ve_rakamalari_asallar.append(i)
# else:
#     print(cift_ve_rakamalari_asallar)




# i=2131239566
# liste=[*str(i)]
# print(liste)



# otomorfik_sayilar=[]
# for i in range(1,1000000):
#     son_rakamlar=""
#     sayinin_karesi=i**2
#     rakamlarin_listesi=[*str(sayinin_karesi)]
#     for j in range(1,len(str(i))+1):
#         son_rakamlar=str(rakamlarin_listesi[-j])+son_rakamlar
#     else:
#         if int(son_rakamlar)==i:
#             otomorfik_sayilar.append(i)
# else:
#     print(otomorfik_sayilar)
    


# sayi=1
# rakamlar_karesi_toplami=0
# mutlu_sayilar=[]
# while sayi<1000:  
#     sayi+=1
#     a=str(sayi)
#     adet=0
#     while adet<10:
#         rakamlar_karesi_toplami=0
#         for j in a:
#             rakamlar_karesi_toplami+=int(j)**2
#         else:
#             if rakamlar_karesi_toplami==1:
#                 mutlu_sayilar.append(sayi)
#                 break
#             else:
#                 adet+=1
#                 a=str(rakamlar_karesi_toplami)
# print(mutlu_sayilar)




# smith_sayilari=[]
# for i in range(2,1000):
#     a=i
#     rakamlar_toplami=0
#     asal_carpanlar_toplami=0
#     asal_sayi_kontrolu=0
#     asal_carpan=[]
#     while a!=1:
#         for j in range(2,a+1):
#             if a%j==0:
#                 for k in range(2,int(j**0.5)+1):
#                     if j%k==0:
#                         break
#                 else:
#                     asal_sayi_kontrolu+=1
#                     a//=j
#                     asal_carpan.append(j)
#                     for k in str(j):
#                         asal_carpanlar_toplami+=int(k)
#     if asal_sayi_kontrolu!=1:
#         for j in str(i):
#             rakamlar_toplami+=int(j)
#         else:
#             if rakamlar_toplami==asal_carpanlar_toplami:
#                 print(i,asal_carpan)
#                 smith_sayilari.append(i)
# else:
#     print(smith_sayilari)




# smith_sayilari=[]
# for i in range(2,1000):
#     a=i
#     rakamlar_toplami=0
#     asal_carpanlar_toplami=0
#     asal_carpanlar=[]
#     asal_mi=1
#     for b in range(2,int(a**0.5)+1):
#         if a%b==0:
#             asal_mi=0
#             break
#     if asal_mi==1:
#         continue 

#     j=2
#     while a!=1:
#         if a%j==0:
#             a//=j
#             asal_carpanlar.append(j)
#             for k in str(j):
#                 asal_carpanlar_toplami+=int(k)
#         else:
#             j+=1 
#     for m in str(i):
#         rakamlar_toplami+=int(m)
#     else:
#         if rakamlar_toplami==asal_carpanlar_toplami:
#             print(i,asal_carpanlar)
#             smith_sayilari.append(i)
# else:
#     print(smith_sayilari)




# smith_sayilari=[]
# for i in range(1000):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         continue
#     asal_carpanlar=[]
#     a=i
#     asal_carpanlar_toplami=0
#     rakamlar_toplami=0
#     while a!=1:
#         for j in range(2,a+1):
#             if a%j==0:
#                 for k in range(2,int(j**0.5)+1):
#                     if j%k==0:
#                         break
#                 else:
#                     asal_carpanlar.append(j)
#                     a//=j
#                     for l in str(j):
#                         asal_carpanlar_toplami+=int(l)
#     for k in str(i):
#         rakamlar_toplami+=int(k)
#     else:
#         if rakamlar_toplami==asal_carpanlar_toplami:
#             smith_sayilari.append(i)
# else:
#     print(smith_sayilari)




# arkadas_sayi_cifti=[]
# for i in range(1,10000):
#     ikinci_sayi=0
#     birinci_sayi=0
#     for j in range(1,i):
#         if i%j==0:
#             ikinci_sayi+=j
#     else:
#         for k in range(1,ikinci_sayi):
#             if ikinci_sayi%k==0:
#                 birinci_sayi+=k
#         else:
#             if birinci_sayi==i and birinci_sayi>ikinci_sayi:
#                 arkadas_sayi=ikinci_sayi,birinci_sayi
#                 arkadas_sayi_cifti.append(arkadas_sayi)
# else:
#     print(arkadas_sayi_cifti)




# sabit_terslik_toplami=[]
# sabitlik_adedi=0
# for i in range(1,10000):
#     ters_i=""
#     for j in str(i):
#         ters_i=j+ters_i
#     else:
#         if i+int(ters_i)==2321:
#             a=i,int(ters_i)
#             sabitlik_adedi+=1
#             sabit_terslik_toplami.append(a)
# else:
#     print(sabitlik_adedi)




# kare_kup_ortak_sayilari=[]
# for i in range(1,100):
#     if int((i**3)**(1/2))==(i**3)**(1/2):
#         kare_kup_ortak_sayilari.append(i)
# else:
#     print(kare_kup_ortak_sayilari)




# a=[]
# for i in range(1,20):
#     a.append(i**2)
# else:
#     print(a)



# rakam_carpan_tekrarlari=[]
# for i in range(1,100):
#     rakam_carpan=1
#     for j in str(i):
#         rakam_carpan*=int(j)
#     else:
#         if rakam_carpan!=0 and (rakam_carpan%i==0 or i%rakam_carpan==0):
#             rakam_carpan_tekrarlari.append(i)
# else:
#     print(rakam_carpan_tekrarlari)




# ters_cift_asal_sayilar=[]
# ters_cift_adedi=0
# for i in range(1,1000000):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break   
#     else:
#         ters_i=""
#         for j in str(i):
#             ters_i=j+ters_i
#         else:
#             if i<int(ters_i):
#                 for k in range(2,int(int(ters_i)**0.5)+1):
#                     if int(ters_i)%k==0:
#                         break
#                 else:
#                     ters_cift_asal_sayilar.append(i)
#                     ters_cift_adedi+=1
# else:
#     print(ters_cift_asal_sayilar)
#     print("""Ters Çift Adedi: 
# """,ters_cift_adedi,sep="")




# ussu_farki_listesi=[]
# for i in range(1,2000):
#     for j in range(1,4):
#         if i**(j+1)-i**j==3840:
#             ussu_farki_listesi.append(i)
# else:
#     print(ussu_farki_listesi)




# ters_rakam_bolunen_sayilar=[]
# for i in range(1,1000):
#     ters_i=""
#     for j in str(i):
#         ters_i=j+ters_i
#     else:
#         if int(ters_i)%i==0:
#             ters_rakam_bolunen_sayilar.append(i)
# else:
#     print(ters_rakam_bolunen_sayilar)




# sayi_listesi=[]
# sayi_adedi=0
# for i in range(1000,10000):
#     rakamlar_carpimi=1
#     for j in str(i):
#         rakamlar_carpimi*=int(j)
#     else:
#         if rakamlar_carpimi%7==0:
#             sayi_listesi.append(i)
#             sayi_adedi+=1
# else:
#     print(sayi_listesi)
#     print(sayi_adedi)




# sayi_lisetesi=[]
# sayi_adedi=0
# for i in range(1,1507):
#     if 1507%i==7 and i%2==1:
#         sayi_lisetesi.append(i)
#         sayi_adedi+=1
# else:
#     print(sayi_lisetesi)
#     print(sayi_adedi)




# for i in range(100000,0,-1):
#     rakam_kontrol=set()
#     if i%11==0:
#         for k in str(i):
#             rakam_kontrol.add(k)
#         else:
#             if len(rakam_kontrol)==len(str(i)):
#                 break
# print(i%9)




# a="1"
# for i in range(2009):
#     a+="0"
# else:
#     a+="1"
#     print(int(a)%44)




# simetrik_toplamlar=[]
# for i in range(1,1000):
#     ters_i=""
#     for j in str(i):
#         ters_i=j+ters_i
#     else:
#         if (i+int(ters_i))**0.5==int((i+int(ters_i))**0.5):
#             simetrik_toplamlar.append(i)
# else:
#     print(simetrik_toplamlar)




# cift_fark_asallari_listesi=[]
# asal_sayi_listesi=[]
# for i in range(2,1000):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         asal_sayi_listesi.append(i)
# else:
#     for i in asal_sayi_listesi:
#         for j in asal_sayi_listesi:
#             if (i-j)%2==0:
#                 cift_asallar=i,j
#                 cift_fark_asallari_listesi.append(cift_asallar)
#     else:
#         cift_fark_asallari_listesi.sort()
#         print(len(cift_fark_asallari_listesi))



# rakam_donusum_sayilari=[]
# for i in range(1,1000):
#     rakamlar_toplami=0
#     rakamlar_carpimi=0
#     for j in range(1,i):
#         if i%j==0:
#             rakamlar_carpimi+=j
#     else:
#         for k in str(i):
#             rakamlar_toplami+=int(k)
#         else:
#             if rakamlar_carpimi==rakamlar_toplami:
#                 rakam_donusum_sayilari.append(i)
# else:
#     print(rakam_donusum_sayilari)
#     print(len(rakam_donusum_sayilari))



# a=1
# b=1
# alternatif_cift_fibonacci_sayilari=[]
# for i in range(10):
#     c=a
#     a=b
#     b=c+b
#     if (a*b)%2==0:
#         d=a,b
#         alternatif_cift_fibonacci_sayilari.append(d)
# else:
#     print(alternatif_cift_fibonacci_sayilari)




# a=1
# b=1
# asal_duzey_fibonacci_sayilari=[]
# fibonacci_adedi=0
# while fibonacci_adedi<20:
#     rakamlar_toplami=0
#     fibonacci_adedi+=1
#     c=a
#     a=b
#     b=b+c
#     for rakam in str(b):
#         rakamlar_toplami+=int(rakam)
#     for asal in range(2,rakamlar_toplami):
#         if rakamlar_toplami%asal==0:
#             break
#     else:
#         asal_duzey_fibonacci_sayilari.append(b)
# print(asal_duzey_fibonacci_sayilari)
         


# asal_sayi_listesi=[]
# ters_asal_farklar_listesi=[]
# for i in range(2,50):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         asal_sayi_listesi.append(i)
# else:
#     for k in asal_sayi_listesi:
#         for j in asal_sayi_listesi:
#             if k>j+10:
#                 fark=str(k-j)
#                 ters_fark=""
#                 for l in fark:
#                     ters_fark=l+ters_fark
#                 else:
#                     if ters_fark==fark:
#                         ters_asal_farklar=k,j
#                         ters_asal_farklar_listesi.append(ters_asal_farklar)
#     else:
#         print(ters_asal_farklar_listesi)




# kup_farki_asal_sayilar_ciftleri_listesi=[]
# for i in range(2,100):
#     kup_farki=i**3-(i-1)**3
#     for j in range(2,kup_farki):
#         if kup_farki%j==0:
#             break
#     else:
#         kup_farki_cifti=i**3-(i-1)**3
#         kup_farki_asal_sayilar_ciftleri_listesi.append(kup_farki_cifti)
# else:
#     print(kup_farki_asal_sayilar_ciftleri_listesi)




# mukemmel_dongu_sayilari=[]
# for i in range(1,1000):
#     ters_i=""
#     for j in str(i):
#         ters_i=j+ters_i
#     else:
#         ters_toplam=i+int(ters_i)
#         mukemmel_kontrol=0
#         for k in range(1,ters_toplam):
#             if ters_toplam%k==0:
#                 mukemmel_kontrol+=k
#         else:
#             if mukemmel_kontrol==ters_toplam:
#                 mukemmel_dongu_sayilari.append(i)
# else:
#     print(mukemmel_dongu_sayilari)




# ardısık_cift_Tam_kareler=[]
# for i in range(2,1000,2):
#     if int((i**2+(i+2)**2)**0.5)==(i**2+(i+2)**2)**0.5:
#         a=i,i+2
#         ardısık_cift_Tam_kareler.append(a)
# else:
#     print(ardısık_cift_Tam_kareler)



# harmonik_ortalama_listesi=[]
# for i in range(1,1000):
#     bolenler_toplami=0
#     for j in range(1,i//2+1):
#         if i%j==0:
#             bolenler_toplami+=1/j
#     else:
#         bolenler_toplami+=1/i
#         harmonik_ortalama=4/bolenler_toplami
#         if harmonik_ortalama==int(harmonik_ortalama):
#             harmonik_ortalama_listesi.append(i)
# else:
#     print(harmonik_ortalama_listesi)




# asal_sayilar=[]
# for i in range(2,50):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         asal_sayilar.append(i)
# asal_carpan_kupu_esitligi_listesi=[]
# for i in range(2,100):
#     asal_carpanlar_kupu_toplami=0
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0 and j in asal_sayilar:
#             asal_carpanlar_kupu_toplami+=j**3
#     else:
#         if asal_carpanlar_kupu_toplami==i:
#             asal_carpan_kupu_esitligi_listesi.append(i)
# else:
#     print(asal_carpan_kupu_esitligi_listesi)
#     print(asal_sayilar)




# otomorfik_sayilari=[]
# for i in range(1,10000):
#     sayinin_karesi=[*str(i**2)]
#     sayi_kendisi_kontrolu=""
#     for j in range(1,len(str(i))+1):
#         sayi_kendisi_kontrolu=sayinin_karesi[-j]+sayi_kendisi_kontrolu
#     else:
#         if int(sayi_kendisi_kontrolu)==i:
#             otomorfik_sayilari.append(i)
# else:
#     print(otomorfik_sayilari)




# mutlu_sayilar=[]
# en_buyuk_tekrar_adedi=-1
# for i in range(1,10000):
#     a=i
#     tekrar_adedi=0
#     while True:
#         rakamlar_kareleri_toplami=0
#         for j in str(a):
#             rakamlar_kareleri_toplami+=int(j)**2
#         else:
#             a=rakamlar_kareleri_toplami
#             tekrar_adedi+=1
#             if tekrar_adedi>15:
#                 break
#         if a==1 and en_buyuk_tekrar_adedi<tekrar_adedi:
#             en_buyuk_tekrar_adedi=tekrar_adedi
#             b=i,en_buyuk_tekrar_adedi
#             mutlu_sayilar.append(b)
#             break
# else:
#     print(b)




# smith_sayilari=[]
# for i in range(2,1000):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         continue
#     a=i
#     j=2
#     rakamlar_toplami=0
#     asal_carpanlar_rakamlari_toplami=0
#     while a!=1:
#         if a%j==0:
#             for k in str(j):
#                 asal_carpanlar_rakamlari_toplami+=int(k)
#             else:
#                 a//=j
#         else:
#             j+=1
#     for l in str(i):
#         rakamlar_toplami+=int(l)
#     else:
#         if asal_carpanlar_rakamlari_toplami==rakamlar_toplami:
#             smith_sayilari.append(i)
# else:
#     print(smith_sayilari)



# cift_asal_sayi_listesi=[]
# asal_sayi_listesi=[]
# for i in range(2,1000):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         asal_sayi_listesi.append(i)
# else:
#     for i in asal_sayi_listesi:
#         if i-2 in asal_sayi_listesi:
#             a=i-2,i
#             cift_asal_sayi_listesi.append(a)
#     else:
#         print(cift_asal_sayi_listesi)



# arkadas_sayilar=[]
# for i in range(1,10000):
#     ilk_bolen=0
#     for j in range(1,i//2+1):
#         if i%j==0:
#             ilk_bolen+=j
#     else:
#         if ilk_bolen>i:
#             ikinci_bolen=0
#             for k in range(1,ilk_bolen//2+1):
#                 if ilk_bolen%k==0:
#                     ikinci_bolen+=k
#             else:
#                 if i==ikinci_bolen:
#                     a=i,ilk_bolen
#                     arkadas_sayilar.append(a)
# else:
#     print(arkadas_sayilar)




# pisagor_ucluleri=[]
# for a in range(1,100):
#     for b in range(1,a):
#         if (a**2+b**2)**0.5==int((a**2+b**2)**0.5):
#             c=b,a
#             pisagor_ucluleri.append(c)
# else:
#     print(pisagor_ucluleri)




# fermat_sayilari=[]
# for i in range(2,10):
#     a=2**i-1
#     for j in range(2,int(a**0.5)+1):
#         if a%j==0:
#             break
#     else:
#         fermat_sayilari.append(i)
# else:
#     print(fermat_sayilari)




# pronic_sayilar=[]
# for i in range(1,20):
#     pronic_sayilar.append(i*(i+1))
# else:
#     print(pronic_sayilar)



# karmasik_polindrom_Sayilari=[]
# for i in range(1,1000):
#     ters_i=""
#     ters_rakamlar_toplami=""
#     rakamlar_toplami=0
#     for j in str(i):
#         ters_i=j+ters_i
#         rakamlar_toplami+=int(j)
#     else:
#         if ters_i==str(i):
#             for k in str(rakamlar_toplami):
#                 ters_rakamlar_toplami=k+ters_rakamlar_toplami
#             else:
#                 if ters_rakamlar_toplami==str(rakamlar_toplami) and rakamlar_toplami>10:
#                     karmasik_polindrom_Sayilari.append(i)
# else:
#     print(karmasik_polindrom_Sayilari)



# onlu_ikili_polindromlar_toplami=0
# onlu_ikili_sayilar=[]
# polindrom_sayilar=[]
# for i in range(1,1000000):
#     ters_i=""
#     for j in str(i):
#         ters_i=j+ters_i
#     else:
#         if int(ters_i)==i:
#             polindrom_sayilar.append(i)
# else:
#     for i in polindrom_sayilar:
#         a=i
#         ikili_sayi=""
#         while i!=1:
#             ikili_sayi+=str(i%2)
#             i//=2
#         else:
#             ikili_sayi+="1"
#             ters_ikili_sayi=""
#             for j in str(ikili_sayi):
#                 ters_ikili_sayi=j+ters_ikili_sayi
#             else:
#                 if ters_ikili_sayi==ikili_sayi:
#                     onlu_ikili_polindromlar_toplami+=a
#                     onlu_ikili_polindromlar=a,int(ikili_sayi)
#                     onlu_ikili_sayilar.append(onlu_ikili_polindromlar)
# print(onlu_ikili_sayilar)
# print(len(onlu_ikili_sayilar))
# print(onlu_ikili_polindromlar_toplami)

# i=int(input())
# ikili_sayi=""
# while i!=1:
#     ikili_sayi+=str(i%2)
#     i//=2
# else:
#     ikili_sayi+="1"
#     ters_ikili_sayi=""
#     print(ikili_sayi)
#     for j in str(ikili_sayi):
#         ters_ikili_sayi=j+ters_ikili_sayi
#     else:
#         if ters_ikili_sayi==ikili_sayi:
#            print("dormammu")




# faktoriyel=1
# faktoriyel_Asallar=[]
# for i in range(2,10):
#     faktoriyel*=i
#     a=0
#     for j in range(2,faktoriyel-1):
#         if (faktoriyel-1)%j==0:
#             break
#     else:
#         a=1
#     for j in range(2,faktoriyel+1):
#         if (faktoriyel+1)%j==0:
#             break
#     else:
#         a=1
#     if a==1:
#         faktoriyel_Asallar.append(i)
# else:
#     print(faktoriyel_Asallar)



# ardısık_sayi_kupu_listesi=[]
# for i in range(1,1000):
#     ardısık_sayi_kupu=i**3+(i+1)**3+(i+2)**3
#     for j in range(2,ardısık_sayi_kupu):
#         if ardısık_sayi_kupu%j==0:
#             break
#     else:
#         ardısık_sayilar=[i,i+1,i+2]
#         ardısık_sayi_kupu_listesi.append(ardısık_sayilar)
# else:
#     print(ardısık_sayi_kupu_listesi)


# rakam_karesi_asal_olan_sayilar=[]
# for i in range(1,100):
#     rakamlar_karesi_toplami=0
#     for j in str(i):    
#         rakamlar_karesi_toplami+=int(j)**2
#     else:
#         rakamlar_karesi_toplami_modu=rakamlar_karesi_toplami%i
#         for k in range(2,rakamlar_karesi_toplami_modu):
#             if rakamlar_karesi_toplami%k==0:
#                 break
#         else:
#             rakam_karesi_asal_olan_sayilar.append(i)
# else:
#     print(rakam_karesi_asal_olan_sayilar)




# faktoriyel_modlu_asallar=[]
# faktoriyel=1
# for i in range(1,100):
#     faktoriyel*=i
#     for j in range(2,faktoriyel-i):
#         if (faktoriyel-i)%j==0:
#             break
#     else:
#         faktoriyel_modlu_asallar.append(i)
# else:
#     print(faktoriyel_modlu_asallar)




# son_iki_basamak_kup_asal_sayilar=[]
# for i in range(3,100):
#     sayinin_kupu=[*str(i**3)]
#     son_iki_basamak=sayinin_kupu[-2]+sayinin_kupu[-1]
#     if int(son_iki_basamak)!=0 and int(son_iki_basamak)!=1:
#         for j in range(2,int(son_iki_basamak)):
#             if int(son_iki_basamak)%j==0:
#                 break
#         else:
#             son_iki_basamak_kup_asal_sayilar.append(i)
#             print(i,son_iki_basamak)
# else:
#     print(son_iki_basamak_kup_asal_sayilar)




# kare_kup_liste=[]
# for i in range(1,1000): 
#     for j in range(1,1000):
#         if int((i**2+j**2)**(1/3))==(i**2+j**2)**(1/3):
#             a=i,j,int((i**2+j**2)**1/3)
#             kare_kup_liste.append(a)
# else:
#     print(kare_kup_liste)



# listem=[]
# for i in range(2,100,2):
#     a=1
#     b=1
#     for j in range(1,i+1):
#         a*=j
#     else:
#         for j in range(1,i+3):
#             b*=j
#         else:
#             c=(a+b)%(i+2)
#             if c == int(c):
#                 d=i,i+2,c
#                 listem.append(d)
# else:
#     print(listem)




# mersenne_sayilari=[]
# for i in range(2,50):
#     for j in range(2,int((2**i-1)**0.5)+1):
#         if (2**i-1)%j==0:
#             break
#     else:
#         mersenne_sayilari.append(2**i-1)
# else:
#     print(mersenne_sayilari)

# https://music.youtube.com/watch?v=E0PuVioACfQ&si=QPh8EqRZlAz_thGj




# pdi_sayilari=[]
# for i in range(1,100000):
#     basamaklar_ussu_toplami=0
#     for j in str(i):
#         basamaklar_ussu_toplami+=int(j)**len(str(i))
#     else:
#         if basamaklar_ussu_toplami==i:
#             pdi_sayilari.append(i)
# else:
#     print(pdi_sayilari)



# leyland_sayilari=[]
# for i in range(2,19):
#     for j in range(2,i):
#         leyland_kontrol=i**j+j**i
#         for k in range(2,int(leyland_kontrol**0.5)+1):
#             if leyland_kontrol%k==0:
#                 break
#         else:
#             leyland_sayilari.append(leyland_kontrol)
# else:
#     print(leyland_sayilari)




# otomorfik_sayilar=[]
# for i in range(1,100000):
#     kontrol=[*str(i**2)]
#     son_basamaklar=""
#     for j in range(1,len(str(i))+1):
#         son_basamaklar=kontrol[-j]+son_basamaklar
#     else:
#         if int(son_basamaklar)==i:
#             otomorfik_sayilar.append(i)
# else:
#     print(otomorfik_sayilar)




# pandigital_asallar=[]
# for i in range(1,100000):
#     for j in str(i):
#         if int(j)>len(str(i)):
#             break
#     else:
#         kontrol_sayisi=[]
#         for k in str(i):
#             if k not in kontrol_sayisi:
#                 kontrol_sayisi.append(k)
#         else:
#             if len(kontrol_sayisi)==len(str(i)):
#                 for l in range(2,i):
#                     if i%l==0:
#                         break
#                 else:
#                     pandigital_asallar.append(i)
# else:
#     print(pandigital_asallar)




# catalan_sayilari=[]
# for n in range(1,10):
#     payda=1
#     pay=1
#     for j in range(1,2*n+1):
#         if j<n+1:
#             payda*=j
#         pay*=j
#     else:
#         payda*=(payda*(n+1))
#         catalan_sayisi=pay/payda
#         catalan_sayilari.append(int(catalan_sayisi))
# else:
#     print(catalan_sayilari)




# ruth_aaron_ciftleri=[]
# for i in range(2,2000):
#     sayi2=i+1
#     sayi1=i
#     a=2
#     asal_sayi_listesi1=[]
#     asal_sayi_listesi1_toplami=0
#     while sayi1!=1:
#         if sayi1%a==0:
#             for k in range(2,int(a**0.5)+1):
#                 if a%k==0:
#                     break
#             else:
#                 asal_sayi_listesi1.append(a)
#                 asal_sayi_listesi1_toplami+=a
#                 sayi1//=a
#         else:
#             a+=1
#     else:
#         for j in range(2,int(sayi2*0.5)+1):
#             if sayi2%j==0:
#                 a=2
#                 asal_sayi_listesi2=[]
#                 asal_sayi_listesi2_toplami=0
#                 while sayi2!=1:
#                     if sayi2%a==0:
#                         for k in range(2,int(a**0.5)+1):
#                             if a%k==0:
#                                 break
#                         else:
#                             asal_sayi_listesi2.append(a)
#                             asal_sayi_listesi2_toplami+=a
#                             sayi2//=a
#                     else:
#                         a+=1
#                 else:
#                     if asal_sayi_listesi1_toplami==asal_sayi_listesi2_toplami:
#                         a=i,i+1
#                         ruth_aaron_ciftleri.append(a)
# else:
#     print(ruth_aaron_ciftleri)




# palindromik_asal_sayilar=[]
# for i in range(2,1000):
#     ters_i=""
#     for j in str(i):
#         ters_i=j+ters_i
#     else:
#         if int(ters_i)==i:
#             for k in range(2,int(i**0.5)+1):
#                 if i%k==0:
#                     break
#             else:
#                 palindromik_asal_sayilar.append(i)
# else:
#     print(palindromik_asal_sayilar)




# sophia_germain_asallari=[]
# for p in range(2,2000):
#     for i in range(2,int(p**0.5)+1):
#         if p%i==0:
#             break
#     else:
#         for j in range(2,int((2*p+1)**0.5)+1):
#             if (2*p+1)%j==0:
#                 break
#         else:
#             sophia_germain_asallari.append(p)
# else:
#     print(sophia_germain_asallari)




# asal_fermat_sayilari=[]
# for n in range(1,15):
#     fermat_sayisi=((2**2)**n)+1
#     for j in range(2,int(fermat_sayisi**0.5)+1):
#         if fermat_sayisi%j==0:
#             break
#     else:
#         asal_fermat_sayilari.append(fermat_sayisi)
# else:
#     print(asal_fermat_sayilari)




# mersenne_mukemmel_sayilari=[]
# for p in range(1,25):
#     mersenne_Sayisi=2**p-1
#     for i in range(2,int(mersenne_Sayisi**0.5)+1):
#         if mersenne_Sayisi%i==0:
#             break
#     else:
#         mersenne_mukemmel_sayilari.append(mersenne_Sayisi)
# print(mersenne_mukemmel_sayilari)




# cift_sayilar=[]
# asal_sayilar=[]
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         asal_sayilar.append(i)
# else:
#     for i in asal_sayilar:
#         for j in asal_sayilar:
#             cift_sayi=i+j
#             if cift_sayi%2==0:
#                 if cift_sayi not in cift_sayilar:
#                     cift_sayilar.append(cift_sayi)
#                     print(i,j,cift_sayi)



# ramanujan_sayilari=[]
# for i in range(1,16):
#     for j in range(1,i):
#         if i>j:
#             ramanujan_sayisi=i**3+j**3
#             ramanujan_sayilari.append(ramanujan_sayisi)
# else:
#     print(ramanujan_sayilari)




# lynchel_Sayilari=[]
# for i in range(1,1000):
#     tekrar_adedi=0
#     a=i
#     while tekrar_adedi!=10:
#         ters_i=""
#         for j in str(i):
#             ters_i=j+ters_i
#         else:
#             kontrol_toplami=int(ters_i)+i
#             ters_kontrol_toplami=""
#             for k in str(kontrol_toplami):
#                 ters_kontrol_toplami=k+ters_kontrol_toplami
#             else:
#                 if int(ters_kontrol_toplami)==kontrol_toplami:
#                     break
#                 else:
#                     tekrar_adedi+=1
#                     i=kontrol_toplami
#     if tekrar_adedi==10:
#         lynchel_Sayilari.append(a)
# else:
#     print(lynchel_Sayilari)




# harshad_niven_sayilari=[]
# for i in range(1,1000):
#     basamaklar_toplami=0
#     for j in str(i):
#         basamaklar_toplami+=int(j)
#     else:
#         if i%basamaklar_toplami==0:
#             harshad_niven_sayilari.append(i)
# else:
#     print(harshad_niven_sayilari)




# ikiz_asal_sayilar_listesi=[]
# asal_sayilar_listesi=[]
# for i in range(2,1000):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         asal_sayilar_listesi.append(i)
# else:
#     for i in asal_sayilar_listesi:
#         for j in asal_sayilar_listesi:
#             if i-2==j:
#                 a=j,i
#                 ikiz_asal_sayilar_listesi.append(a)
#     else:
#         print(ikiz_asal_sayilar_listesi)




# asal_sayilar=[]
# wieferich_asal_Sayilari=[]
# for i in range(2,10000):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         asal_sayilar.append(i)
# else:
#     for i in asal_sayilar:
#         if (2**(i-1))%(i**2)==1:
#             wieferich_asal_Sayilari.append(i)
#     else:
#         print(wieferich_asal_Sayilari)




# a=2
# sylvester_sayilari=[]
# for i in range(1,8):
#     a=a*(a-1)+1
#     for j in range(2,int(a**0.5)+1):
#         if a%j==0:
#             break
#     else:
#         sylvester_sayilari.append(a)
# else:
#     print(sylvester_sayilari)




