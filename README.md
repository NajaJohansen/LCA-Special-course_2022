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
The project have been performed by 6 master students as part of a 5 ects point course at the Technical University of Denmark (DTU). The project have had the focus areas: 
  1) Create an EPD search engine in python that can connect with Ecoportalen through an API and produce a library of EPDs that a categorised in different building component categories. (LÆRKE OG NAJA RETTER)
  2) Create a grasshopper script that can use the library and relate the building components with the correct EPDs and thus caluclate CO2 impact of different constructions and subsequently an entire building. The results of the CO2 calculatines is given in ranges. 
  3) Visulaize the results as boxplot that indicates the range of possible CO2 impact of a building, depning on which materaial combination 


By conveying LCA results with a range instead of a single number, designers are to a greater extend made aware of the impact of their decisions. This will help integrate sustainble thinking into building design

The goal is to develop tools that will allow the user to perform LCA analysis in a 
more dynamic and parametric way.
The project is a 3-week course performed by Lærke Høvsgaard Vejsnæs and Terese Pagh, both
Architectural Engineering master students at the Technical University of Denmark.
This is done in collaboration with the research department BUILD, at Aalborg University.
BUILD is the developer of LCAbyg Web API, which is used to compute the LCA results. 
It is the beginning of a bigger project which will lead up to our thesis project in fall 2022.
As we are architectural engineering students our expertise lies in LCA analysis of buildings, but we are very passionate about 
digital tools that can help make the building industry become more efficient.
The code is built with the intent to implement a user interface with required user inputs. At present, hardcoded variables performs as placeholders for imaginary user inputs. 
We will be updating and adding to this repository frequently, and we will very much appreciate comments and suggestions 
if anyone is interested. 

### Requesting EPD data via API
A large part of this project is about getting the EPD data digitally, which is possible 

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

![<img src="doc/diagrams/workflow_jan_22.png"/>](doc/diagrams/workflow_jan22.png "Workflow")

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

