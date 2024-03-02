#  Fire prediction -  Data Camp 2023

Authors: Matthis Guerin, Valentina HU, Adrien Oleksiak, Manuel Nkegoum, Nicolas Saint, Selma Zarga


## Dataset 

Our dataset includes various features, and we are excluding non-essential data. Below are the sources for the datasets used:

- [Weather Dataset](https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32)
- [Solar + Wind Speed Data](https://odre.opendatasoft.com/explore/dataset/rayonnement-solaire-vitesse-vent-tri-horaires-regionaux/information/?flg=fr-fr&disjunctive.region)
- [Classified Stations and Tourist Communes - France](https://public.opendatasoft.com/explore/dataset/economicref-france-commune-classement-touristique/table/?flg=fr-fr&disjunctive.reg_name&disjunctive.dep_name&disjunctive.epci_name)
- [Population Density per Commune](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.insee.fr%2Ffr%2Fstatistiques%2Ffichier%2F5039883%2FFET2021-19.xlsx&psig=AOvVaw229C_TW9QCmiJcLoIMaztC&ust=1709491158758000&source=images&cd=vfe&opi=89978449&ved=0CAgQrpoMahcKEwiI8L_7nNaEAxUAAAAAHQAAAAAQBA)
- [Wildfire Information](https://www.data.gouv.fr/fr/datasets/base-de-donnees-sur-les-incendies-de-forets-en-france-bdiff/)


## Getting started

### Install
To run a submission and the notebook you will need the dependencies listed in ``requirements.txt``. You can install the dependencies with the following command-line:

```bash 
pip install -U -r requirements.txt
```

If you are using conda, we provide an ``environment.yml`` file for similar usage.

### Challenge description
Get started on this RAMP with the dedicated notebook.

### Test a submission
The submissions need to be located in the submissions folder. For instance for my_submission, it should be located in ``submissions/my_submission``.

To run a specific submission, you can use the 
``ramp-test`` command line:

```bash 
ramp-test --submission my_submission
```

You can get more information regarding this command line:

``` bash  
ramp-test --help
```

