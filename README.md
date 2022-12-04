[![AGPL License][license-shield]][license-url]

<br />
<div align="center">
<h3 align="center">Parametric Life-Cycle Assessment in Early-stage Building Design</h3>
  <p align="center">
    Tool for flexible LCA analysis of buildings
    <br />
    <a href="https://github.com/NajaJohansen/GrassHopper_Course"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NajaJohansen/GrassHopper_Course/pulls">Pull requests</a>
    ·
    <a href="https://github.com/NajaJohansen/GrassHopper_Course/issues">Elaboration of unsolved issues</a>
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Concept</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
The project has been performed by 6 master students as part of a 5 ECTS point course at the Technical University of 
Denmark (DTU). The project started with the idea that by conveying LCA results with a range instead of a single number, 
designers are to a greater extent made aware of the impact of their decisions. This will help integrate sustainable 
thinking into the early stage of building design. Further, the data should be based on project specific EPD’s instead of generic data. 

The project had the following goals: 
1.	Investigate the market of LCA tools and figure out strength and shortcomings of a selection of existing tools and carry out interviews with industry experts.
2.	Create an EPD search engine in python that can connect with ECO Portal through an API and produce a library of EPDs with their characterization factors for Global Warming Potential (GWP), lifetime, density, and functional unit.
3.	Use existing categorizing system from the different EPD operators to categorize the EPDs depending on which type of product they describe and which type of component they can be a part of. 
4.	Create a grasshopper script that can sort and quantify building components and relate them to EPDs that are relevant for the components. The CO2 impacts of the different components and the entire building can then be calculated as ranges of varied materials combinations in the components.
5.	Visualize the results as boxplot that indicates the range of possible CO2 impact of a building, depending on the material choices.

### Existing LCA tools
The project started with a dive into five LCA tools that were developed for different software and for various stages 
of the building design, from early stage to documentation in planning stage. In the folder 
[Flowcharts](figures/Flowcharts) of the workflow with different LCA tools are located. 
The flowchart is based on our expression of the tools and are not crosschecked 
with the developers of the tool. The LCA tools that have been examined is: 
- DesignLCA, developed by Graphisoft and with input from Lenager group. The tool is made for Archicad and gives live results and has implemented a simple energy calculator. The user has to manually assign CO2 data to the materials or use a library with predefined constructions (NAJA MÅ GERNE RETTE)
- LCA Platform, developed by Arkitema and COWI. The tool is divided in two; LCA documentation and LCA design. LCA documentation is for documentation behind the final LCA of project. It is going to be a mutual platform for the Danish building industry, which aim is to secure that across companies the LCA, they are performing have the same level of documentation. The tool can create a JSON file that ca be used in LCAbyg. The other tool; LCA Design is developed for Revit, gives live results in a browser window. 
- CardinalLCA is developed by J. Chen K. Kharbanda and H Loganathan as a plugin for Grasshopper. The tool is designed for early stage LCA and gives live results and visualizations in Rhino. The users can assign materials for the building geometry through the EC3 database or the ICE database. Here they have the option to choose specific data or to create average data. The average data can be found through different filters e.g. by geographical scope.
- ACT – A Carbon Tool, created in Speckle (LÆRKE SKRIVER NOGET)
- LCA:ARK, developed by C.F. Møller and is essentially a grasshopper script. The script can extract quantify the masses of various building components from a rhino model and user can assign different predefined solutions to the component. The script can create a JSON file that can be used in LCAbyg. 

A variety of tools have been developed to ease LCA calculations. They have different strengths and shortcomings. The clear strength of Design LCA, ACT and Cardinal LCA is that they are free whereas the other tools requires that you buy a license or make an agreement with the developers. CardinalLCA is unfortunately no longer maintained and one of the databases behind it is not properly working. ACT requires knowledge of the workflow behind Speckle (LÆRKE MÅ GERNE UDDBYE MED STRENGHT/SHORT COMINGS OF SPEKLE). Design LCA is quite intuitive to use, but the mapping of materials requires some work. The tools DesignLCA, LCA Design, Cardinal LCA, ACT and LCA:ARK is all for early-stage design. 
In the early stage many decisions about the building materials are either not taken or unsure, thus conveying the result of the LCA as an interval is a great way to illustrate that uncertainty, thus we have chosen that the results from our tool should be represented as ranges. Cardinal LCA and LCA:ARK convey the results in this way. Our tool is differentiated from LCA:ARK by being open source and based on EPD, whereas LCA:ARK used the database OEKOBAU, with the possibility of implementing EPDs. CardinalLCA is based upon an American database and a British database, where the aim with our tools is to have access to the database of various EPD database operators. 

### Requesting EPD data via API
A large part of this project is about getting the EPD data digitally, which is possible 

### Categorization of EPDs
To use the different EPDs it is necessary to categorize them to match the different building components as well as 
the product types within these components and material types within the products. For example, the building component 
“exterior wall” has the lower levelled products; “façade”, “insulation”, “structure”, “interior board” and 
“interior surface”. Within these lower levelled products several material types are defined. E.g., the product “façade” 
has the material options “brick”, “wood”, “stone” etc. These categorization classifications are essential to structure 
the data subtracted from the EPDs into relevant groups. The level structure for exterior walls can be seen in 
[category diagram](figures/Levels_categories.png).
Though, the current EPDs are structured differently depending on the EPD operator (e.g., IBU – Institute Baum und 
Umwelt, EPD Denmark etc.). Within the ECO Portal the categorizations are adopted form the respective operator, which 
creates issues due to the categorization not being streamlined and equally elaborated. To reach the fully potential 
of this project these categorizations must be comparable and well-defined across all the different EPD programs. 
This definition is already in process. The EPD operators contributing to the ECO Platform agreed to work on a 
harmonization of among others the Product Category Rules (PCR). This might result in possibility of fulfilling the 
project’s goal further in the future.
However, for now it was necessary to split the project into two branches. One where the relevant EPDs are collected 
via the API and distributed into the wanted categories, and another branch that creates the wanted LCA ranged output from a 3D model. 
As a proof of concept an excel file was made to show the outcome from the LCA script in grasshopper. 
In this file the desired structure of the EPDs were defined. In this excel file  265 EPDs were summarized 
into building components, products, and materials to be used in the script.  


<!-- GETTING STARTED -->
## Getting Started
This project can be approached as one large project or two smaller, the Grasshopper part and the Python part, which 
can be worked with individually. Prerequisites 1 to 5 are for running the Python code, while the rest are for running
the Grasshopper script. 

### Prerequisites
1. Clone the repo
   ```sh
   git clone https://github.com/NajaJohansen/GrassHopper_Course.git
   ```
2. Install Python version 3.10
3. For python install requests
   ```sh
   $ python -m pip install requests
   ```
4. [Register](https://data.eco-platform.org/registration.xhtml) for a ECO Portal user account or [this guide](https://data.eco-platform.org/static/doc/ECO_Portal_API_Howto_Obtain_a_Token.pdf)
5. [Create a token](https://data.eco-platform.org/static/doc/ECO_Portal_API_Howto_Obtain_a_Token.pdf) for access to use the API
6. Install Rhino and Grasshopper
7. For Grasshopper get DecondingSpaces Toolbox
8. for Grasshopper get R 3.4.4


<!-- CONCEPT -->
## Concept

![<img src="figures/Flowcharts/OurProject.png"/>](figures/Flowcharts/OurProject.png "Workflow")

![<img src="figures/Levels_categories.png"/>](figures/Levels_categories.png "Workflow")

<!-- USAGE SPECIFICATIONS -->
## Usage specifications
Here are some practical tips for using the scripts and code and what you should be aware of.

### Usage of Grasshopper script
For the visualization of results the boxplot-component from the 
[DecodingSpaces Toolbox](https://toolbox.decodingspaces.net/) is used. To use these components R 3.4.4 is also required.  
The ‘toggle’ should be put to true and results for the different building 
components are selected through the drop-down menu ‘Item selector’. 

### Usage of python scripts
It is important to add your ECO Portal token to be allowed to 


<!-- CREATORS -->
## Creators
- Andreas Sode Vest (s173798)
- Lærke Vejsnæs (s173832)
- Naja Johansen (s184525)
- Anna Kristina Schjerbeck (s161709)
- Christian Oettinger (s173838)
- Manja Nørrekær Lund (s173803)

<!-- CONTRIBUTING -->
## Contributing
This project can be the beginning of a larger project with a lot of potential. 
We therefore strongly encourage further work,
which can help develop the project and make EPD data more available. 
You are welcome to create a [pull request](https://github.com/NajaJohansen/GrassHopper_Course/pulls) or 
[create a new fork](https://github.com/NajaJohansen/GrassHopper_Course/fork).
If you want a good place to start then take a look at the 
[issues](https://github.com/NajaJohansen/GrassHopper_Course/issues) or see where to 
[contribute](https://github.com/NajaJohansen/GrassHopper_Course/contribute). If you do contribute, please share your
great work, so we can build a great projects together.

<!-- LICENSE -->
## License
Distributed under the AGPL License. See [LICENSE.md](LICENSE.md) for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/NajaJohansen/GrassHopper_Course/contribute
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/NajaJohansen/GrassHopper_Course/fork
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/NajaJohansen/GrassHopper_Course/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/NajaJohansen/GrassHopper_Course/issues
[license-shield]: https://img.shields.io/badge/LICENSE-GNU%20AGPL-lightgrey?style=for-the-badge&logo=gnu
[license-url]: https://www.gnu.org/licenses/agpl-3.0.en.html

