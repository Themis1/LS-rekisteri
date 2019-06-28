# LS-rekisteri  

## - Lainsäädäntörekisteri -  
***
  
Tarkoituksena on luoda rekisteri maa- ja metsätalousministeriön Ruokaosaston lainsäädännön seurantaa varten.  
Aluvaiheessa rekisteriin tallennetaan valtioneuvoston asetukset ja ministeriön asetukset sekä muutosasetus, jolla niitä muutetaan.  
Tarkoitus olisi myös tallentaa kaikki osaston lait (ja asetukset), ja linkittää niihin käynnissä olevat muutokset.  
***  
### Taulut  
Tietokantaan tallennetaan taulut  
* VNa (valtioneuvoston asetus)  
* MMMa (maa- ja metsätalousministeriön asetus)  
* Valmistelija  
* Käyttäjä  
  
Kullakin asetuksella on vastuuvalmistelija. Tauluun voitaisiin mahdollisesti tallentaa myös muita valmistelijoita, mutta se ei tässä vaiheessa ole välttämätöntä.  
Tietokannan käyttäjä ja valmistelija voivat olla eri henkilöt. Siksi molemmille on omat taulut.  

[Sovellus](https://ls-rekisteri.herokuapp.com/)  

[Käyttöohje](https://github.com/Themis1/LS-rekisteri/blob/master/dokumentaatio/kayttoohje.md)

[Asennusohje](https://github.com/Themis1/LS-rekisteri/blob/master/dokumentaatio/asennusohje.md)

[Käyttötapauksia](https://github.com/Themis1/LS-rekisteri/blob/master/dokumentaatio/user_story.md)

[Tietokantakaavio](https://github.com/Themis1/LS-rekisteri/blob/master/dokumentaatio/LS-rekisteri_kaavio.png)



### Mahdollisuus laajennukseen

Tietokantaa on tarkoitus laajentaa koskemaan myös lakeja ja niihin liittyviä hallituksen esityksiä (HE). Nämä on merkitty tietokantakaavioon keltaisella.  
Lisäksi asetuksiin olisi tarkoitus lisätä myöhemmin oma taulunsa muutosasetuksille. Tämäkin on merkitty keltaisella.  

### Puutteita  

Tietokannasta jäi ajanpuutteen vuoksi puuttumaan suuri osa kyselyistä sekä paremmat linkit taulujen välillä. Tarkoitus oli myös toteuttaa vetovalikko kuhunkin asetukseen, josta olisi voinut valita asetusta valmistelevan valmistelijan. Tämä jäi toimimattomaksi, joten poistin sen palautetusta versiosta.  
Tärkein puutos, joka vaikuttaa käyttöön, on edellä mainittu muutosasetus-taulu, jonka suunnittelen vielä lisääväni myöhemmin.  
***
