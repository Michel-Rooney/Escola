Algoritmo "Q15"
Var
   n1, n2, n3 : Caracter
   i1, i2, i3 : inteiro
   a1, a2, a3, med_ari_idade, med_ari_altura, med_geo_altura, med_geo_idade : real


Inicio
      escreva("Nome1: ")
      leia(n1)
      escreva("Idade1: ")
      leia(i1)
      escreva("Altura1: ")
      leia(a1)
      escreva("Nome2: ")
      leia(n2)
      escreva("Idade2: ")
      leia(i2)
      escreva("Altura2: ")
      leia(a2)
      escreva("Nome3: ")
      leia(n3)
      escreva("Idade3: ")
      leia(i3)
      escreva("Altura3: ")
      leia(a3)
      med_ari_idade <- (i1+i2+i3)/3
      med_ari_altura <- (a1+a2+a3)/3
      
      med_geo_altura <- (a1*a2*a3)/3
      med_geo_idade <- (i1*i2*i3)/3
      
      escreva(" Nomes: ", n1, n2, n3)
      escreva(" Idades: ", i1, i2, i3)
      escreva(" Alturas: ", a1, a2, a3)
      escreva(" Media aritimetica idade ", med_ari_idade)
      escreva(" Media aritimetica altura ", med_ari_altura)
      escreva(" Media geometrica idade ", med_geo_idade)
      escreva(" Media geometrica idade ", med_geo_idade)
      
      


Fimalgoritmo