#include <ctype.h>
#include <stdio.h>
#include <string.h>
#define COMUNI "file.txt"
int main()
{
	char codice[16];
int z=0;
int b=0;
int countvocali = 0;
int countcons = 0;
int countvocali2=0;
int countcons2=0;
char tconsonanti[] = { 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' };
char tvocali[]={ 'a','e','i','o','u'};
char num[] = {'0','1','2','3','4','5','6','7','8','9'};
char cognome[10];
int input;
printf("1 Per creare codice fiscale \n 2 Scrivere codice fiscale\nInserire:\t");
scanf("%d",&input);
if(input==1)
{
printf("Inserire cognome\t");
scanf("%s",cognome);
int x=strlen(cognome);
char vocali[x];
char cons[x];
for(int i=0;i<x;i++)
{
	switch(cognome[i])
	{
    	case 'a':
    	{
        	vocali[z]='a';
        	z++;countvocali++;
        	break;
    	}
     	case 'e':
    	{
        	vocali[z]='e';
        	z++;countvocali++;
        	break;
    	}
     	case 'i':
    	{
        	vocali[z]='i';
        	z++;countvocali++;
        	break;
    	}
     	case 'o':
    	{
        	vocali[z]='o';
        	z++;countvocali++;
        	break;
    	}
     	case 'u':
    	{
        	vocali[z]='u';
        	z++;
        	break;
    	}default:
    	{
       	cons[b]=cognome[i];
       	b++;countcons++;
       	break;
    	}
  	 
	}
}
	if(countcons>=3)
	{
    	for(int i=0;i<3;i++)
    	{
        	codice[i]=cons[i];
      	 
    	}
	}else if(countcons==2)
	{
    	for(int i=0;i<2;i++)
    	{
        	codice[i]=cons[i];
    	}
    	codice[2]=vocali[0];
  	 
	}else if(countcons==1 && countvocali==2)
	{
    	codice[0]=cons[0];
    	codice[1]=vocali[0];
    	codice[2]=vocali[1];
  	 
	}else if(countcons==1 && countvocali==1)
	{
    	codice[0]=cons[0];
    	codice[1]=vocali[0];
    	codice[2]='x';
   	 
	}else if(countcons==0 && countvocali==2)
	{
    	for(int i=0;i<2;i++)
    	{
        	codice[i]=vocali[i];
    	}
    	codice[2]='x';
     	 
  	 
	}
   
 	printf("\n");
   
	int s=0;
	int l=0;
	printf("Inserire nome\t");
	char nome[100];
	scanf("%s",nome);
	int k=strlen(nome);
	char vocali2[k];
	char cons2[k];

	for(int i=0;i<k;i++)
{
	switch(nome[i])
	{
    	case 'a':
    	{
        	vocali2[s]='a';
        	s++;countvocali2++;
        	break;
    	}
     	case 'e':
    	{
        	vocali2[s]='e';
        	s++;countvocali2++;
        	break;
    	}
     	case 'i':
    	{
        	vocali2[s]='i';
        	s++;countvocali2++;
        	break;
    	}
     	case 'o':
    	{
        	vocali2[s]='o';
        	s++;countvocali2++;
        	break;
    	}
     	case 'u':
    	{
        	vocali2[s]='u';
        	s++;countvocali2++;
        	break;
    	}default:
    	{
       	cons2[l]=nome[i];
      	l++;countcons2++;
       	break;
    	}
  	 
	}
}
  if(countcons2>=4)
	{
      	codice[3]=cons2[0];
      	codice[4]=cons2[2];
      	codice[5]=cons2[3];
    	 
	}
	else  if(countcons2==3)
	{
    	int reset=0;
    	for(int i=3;i<6;i++)
    	{
        	codice[i]=cons2[reset];
       	reset++;
    	}
   	 
	}
	else if(countcons2==2)
	{
    	int reset=0;
    	for(int i=3;i<5;i++)
    	{
        	codice[i]=cons2[reset];
       	reset++;
    	}
    	codice[5]=vocali2[0];
   	 
	}
	else if(countcons==1 && countvocali==2)
	{
    	codice[3]=cons[0];
    	codice[4]=vocali[0];
    	codice[5]=vocali[1];
 	 
	}else if(countcons2==1 && countvocali2==1)
	{
    	codice[3]=cons2[0];
    	codice[4]=vocali2[0];
    	codice[5]='x';
   	 
	}else if(countcons2==0 && countvocali2==2)
	{   int reset=0;
    	for(int i=3;i<5;i++)
    	{
        	codice[i]=vocali2[reset];
        	reset++;
    	}
    	codice[5]='x';
     	 
  	 
	}
	printf("\n");
    
	char salva[1];
	char giorno[2];
	char day[2];
	int mese;
	char month[1];
	char anno[1];
	char sesso[7];
 
 for(int i=0;i<6;i++)
 {
 	codice[i]=toupper(codice[i]);
 }
   printf("Inserire sesso M o F\t");
	scanf("%s",sesso);
    
	printf("Inserire anno di nascita\t");
    	scanf("%s",anno);
     	int num1 = atoi(anno);
     		if(num1 >= 10)
	{
    	codice[6] = '0' + (num1 / 10 % 10);
    	codice[7] = '0' + (num1 % 10);    
	} else
	{
   	 
    	codice[6] = '0';             	 
    	codice[7] = '0' + num1;        	 
	}
printf("\n");
 	printf("Inserire mese di nascita\t");
         	scanf("%d",&mese);
switch(mese)
{
	case 1:
	codice[8]='A';
	break;
	case 2:
   codice[8]='B';
	break;
	case 3:
   codice[8]='C';
	break;
	case 4:
  codice[8]='D';
	break;
	case 5:
	codice[8]='E';
	break;
	case 6:
   codice[8]='H';
	break;
	case 7:
   codice[8]='L';
	break;
	case 8:
 codice[8]='M';
	break;
	case 9:
	codice[8]='P';
	break;
	case 10:
	codice[8]='R';
	break;
	case 11:
	codice[8]='S';
 	break;
 	case 12:
   codice[8]='T';
	break;
	default:
	printf("\nerrore nel inserimento del mese\n");
	return 0;
	break;
}

printf("\nInserire giorno di nascita\t");
scanf("%s", giorno);
int num2 = atoi(giorno);
if (sesso[0] == 'm' || sesso[0] == 'M')
{  
 
	if(num1 >= 10)
	{
    	codice[9] = '0' + (num2 / 10 % 10);
    	codice[10] = '0' + (num2 % 10);    
	} else
	{
   	 
    	codice[9] = '0';             	 
    	codice[10] = '0' + num2;        	 
	}
printf("\n");
}
else
{
 	num2 = num2 + 40;
 	codice[9] = '0' + (num2 / 10 % 10);
 	codice[10] = '0' + (num2 % 10);  
}
FILE *fp;
char provincia[100];
char cc[100];
char comune[100];
char comunefile[100];
printf("Inserisci comune\t");
scanf("%s", comune);
fp=fopen(COMUNI,"r");
if(fp)
{
 while(fscanf(fp,"%s %s %s\n",cc,comunefile,provincia)!=EOF)
 	{
     	if(strcmp(comune,comunefile)==0)
     	{
         	break;
     	}
 	}
}
else
{
	printf("errore");
}
fclose(fp);
int jo=0;
char bruh;
for(int i=11;i<16;i++)
{
    bruh = toupper(cc[jo]);
   	codice[i]=bruh;
   	jo++;
}
int intercodice=0;
for(int i=0;i<15;i=i+2)
{
  	char c = toupper(codice[i]);
	switch(c)
	{  
 	 
   	 
   	case 'A':
    	intercodice+=1;
    	break;
     	case 'B':
    	intercodice+=0;
    	break;
     	case 'C':
    	intercodice+=5;
    	break;
     	case 'D':
    	intercodice+=7;
    	break;
     	case 'E':
    	intercodice+=9;
    	break;
     	case 'F':
    	intercodice+=13;    
    	break;
     	case 'G':
    	intercodice+=15;
    	break;
     	case 'H':
    	intercodice+=17;
    	break;
     	case 'I':
    	intercodice+=19;
    	break;
     	case 'J':
    	intercodice+=21;
    	break;
     	case 'K':
    	intercodice+=2;
    	break;
     	case 'L':
    	intercodice+=4;    
    	break;
      	case 'M':
    	intercodice+=18;
    	break;
     	case 'N':
    	intercodice+=20;
    	break;
     	case 'O':
    	intercodice+=11;
    	break;
     	case 'P':
    	intercodice+=3;
    	break;
     	case 'Q':
    	intercodice+=6;
    	break;
     	case 'R':
    	intercodice+=8;    
    	break;
     	case 'S':
    	intercodice+=12;
    	break;
     	case 'T':
    	intercodice+=14;
    	break;
     	case 'U':
    	intercodice+=16;
    	break;
     	case 'V':
    	intercodice+=10;
    	break;
     	case 'W':
    	intercodice+=22;
    	break;
     	case 'X':
    	intercodice+=25;
    	break;
     	case 'Y':
    	intercodice+=24;    
    	break;
     	case 'Z':
    	intercodice+=23;    
    	break;
     	case '0':
    	intercodice+=1;
    	break;
     	case '1':
    	intercodice+=0;
    	break;
     	case '2':
    	intercodice+=5;
    	break;
     	case '3':
    	intercodice+=7;
    	break;
     	case '4':
    	intercodice+=9;
    	break;
     	case '5':
    	intercodice+=13;   
    	break;
     	case '6':
    	intercodice+=15;
    	break;
     	case '7':
    	intercodice+=17;
    	break;
     	case '8':
    	intercodice+=19;
    	break;
     	case '9':
    	intercodice+=21;
    	break;
    	default:
    	break;
}
}

for(int i=1;i<15;i=i+2)
{
	char c = toupper(codice[i]);
	switch(c)
	{
     	case 'A':
    	intercodice+=0;
    	break;
     	case 'B':
    	intercodice+=1;
    	break;
     	case 'C':
    	intercodice+=2;
    	break;
     	case 'D':
    	intercodice+=3;
    	break;
     	case 'E':
    	intercodice+=4;
    	break;
     	case 'F':
    	intercodice+=5;
    	break;
     	case 'G':
    	intercodice+=6;
    	break;
     	case 'H':
    	intercodice+=7;
    	break;
     	case 'I':
    	intercodice+=8;
    	break;
     	case 'J':
    	intercodice+=9;
    	break;
     	case 'K':
    	intercodice+=10;
    	break;
     	case 'L':
    	intercodice+=11;
    	break;
      	case 'M':
    	intercodice+=12;
    	break;
     	case 'N':
    	intercodice+=13;
    	break;
     	case 'O':
    	intercodice+=14;
    	break;
     	case 'P':
    	intercodice+=15;
    	break;
     	case 'Q':
    	intercodice+=16;
    	break;
     	case 'R':
    	intercodice+=17;
    	break;
     	case 'S':
    	intercodice+=18;
    	break;
     	case 'T' :
    	intercodice+=19;
    	break;
     	case 'U':
    	intercodice+=20;
    	break;
     	case 'V':
    	intercodice+=21;
    	break;
     	case 'W':
    	intercodice+=22;
    	break;
     	case 'X':
    	intercodice+=23;
    	break;
     	case 'Y':
    	intercodice+=24;
    	break;
     	case 'Z':
    	intercodice+=25;
    	break;
    	case '0':
    	intercodice+=0;
    	break;
     	case '1':
    	intercodice+=1;
    	break;
     	case '2':
    	intercodice+=2;
    	break;
     	case '3':
    	intercodice+=3;
    	break;
     	case '4':
    	intercodice+=4;
    	break;
     	case '5':
    	intercodice+=5;   
    	break;
     	case '6':
    	intercodice+=6;
    	break;
     	case '7':
    	intercodice+=7;
    	break;
     	case '8':
    	intercodice+=8;
    	break;
     	case '9':
    	intercodice+=9;
    	break;
    	default:
    	break;
   	 
	}
}
char tuttelettere[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
printf("\n%s",codice);
printf("%c",tuttelettere[intercodice % 26]);
  printf("\nNome: ");
for(int i=0;i<3;i++)
{
	printf("%c",codice[i]);
}
	printf("\nCognome: ");
	for(int i=3;i<6;i++)
{
	printf("%c",codice[i]);
}
printf("\nAnno: ");
	for(int i=6;i<8;i++)
{
	printf("%c",codice[i]);
}
printf("\nMese: ");
	printf("%c",codice[8]);

printf("\nGiorno: ");
	for(int i=9;i<11;i++)
{
	printf("%c",codice[i]);
}
printf("\nComune: ");
for(int i=0;i<5;i++)
{
   printf("%c",cc[i]); 
}
printf("\nCodice di verifica: ");
printf("%c",tuttelettere[intercodice % 26]);

}else if(input==2)
{
    char mio[16];
      printf("Inserire codice fiscale:\t");
      scanf("%s",mio);
      printf("\nNome: ");
for(int i=0;i<3;i++)
{
	printf("%c",mio[i]);
}
	printf("\nCognome: ");
	for(int i=3;i<6;i++)
{
	printf("%c",mio[i]);
}
printf("\nAnno: ");
	for(int i=6;i<8;i++)
{
	printf("%c",mio[i]);
}
printf("\nMese: ");
switch(mio[8])
{
	case 'A':
	printf("Gennario");
	break;
	case 'B':
   	printf("Febbraio");
	break;
	case 'C':
   	printf("Marzo");
	break;
	case 'D':
  	printf("Aprile");
	break;
	case 'E':
	printf("Maggio");
	break;
	case 'H':
   	printf("Giugno");
	break;
	case 'L':
   	printf("Luglio");
	break;
	case 'M':
 	printf("Agosto");
	break;
	case 'P':
		printf("Settembre");
	break;
	case 'R':
		printf("Ottobre");
	break;
	case 'S':
	printf("Novembre");
 	break;
 	case 'T':
 	printf("Dicembre");
	break;
	default:
	break;
}
printf("\nGiorno: ");
	for(int i=9;i<11;i++)
{
	printf("%c",mio[i]);
}

FILE *fp;
char provincia[100];
char cc[100];
int baby=11;
char cb[4];
char comune[100];
char comunefile[100];
for(int i=0;i<5;i++)
{
    cb[i]=mio[baby];
    baby++;
}

fp=fopen(COMUNI,"r");
if(fp)
{
 while(fscanf(fp,"%s %s\n",cc,comunefile,provincia)!=EOF)
 	{
     	if(strcmp(cc,cb)==0)
     	{
         printf("\nComune: ");
         printf("%s",comunefile);
     	}
 	}
}
else
{
	printf("errore");
}
fclose(fp);
printf("\nCodice di verifica: ");
printf("%c",mio[15]);
}
return 0;



}



























