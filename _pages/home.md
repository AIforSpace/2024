---
layout: project
urltitle:  "Learning 3D Generative Models"
title: "Learning 3D Generative Models"
categories: cvpr, workshop, computer vision, computer graphics, deep learning, generative modeling, visual learning, simulation environments, robotics, machine learning, reinforcement learning
permalink: /
favicon: /static/img/ico/favicon.png
bibtex: true
paper: true
acknowledgements: ""
---

<br>
<div class="row header-row">
  <div class="col-xs-12 header-img">  
    <center><h1>Learning 3D Generative Models</h1></center>
    <center><h2>CVPR 2020 Workshop, Seattle, WA</h2></center>
    <center><span style="font-weight:400;">14th of June 2020</span></center>
    <!--<center><span style="color:#e74c3c;font-weight:400;">Time and Location TBD</span></center>-->
    <br/>
  </div>
</div>

<hr>

<!-- <div class="row" id="">
  <div class="col-md-12">
    <img src="{{ "/static/img/splash.png" | prepend:site.baseurl }}">
    <p> Image credit: [1, 2, 7, 12, 6, 4, 5]</p>
  </div>
</div> -->

<br>
<div class="row" id="intro">
  <div class="col-xs-12">
    <h2>Introduction</h2>
  </div>
</div>
<div class="row">
  <div class="col-xs-12">
    <p>
      The past several years have seen an explosion of interest in generative modeling: unsupervised models which learn to synthesize new elements from the training data domain. Such models have been used to breathtaking effect for generating realistic images, especially of human faces, which are in some cases indistinguishable from reality. The unsupervised latent representations learned by these models can also prove powerful when used as feature sets for supervised learning tasks.
    </p>
    <p>
      Thus far, the vision community's attention has mostly focused on generative models of 2D images. However, in computer graphics, there has been a recent surge of activity in generative models of three-dimensional content: learnable models which can synthesize novel 3D objects, or even larger scenes composed of multiple objects. As the vision community turns from passive internet-images based vision toward more <i>embodied</i> vision tasks, these kinds of 3D generative models become increasingly important: as unsupervised feature learners, as training data synthesizers, as a platform to study 3D representations for 3D vision tasks, and as a way of equipping an embodied agent with a 3D `imagination' about the kinds of objects and scenes it might encounter.
    </p>
    <p>
     With this workshop, we aim to bring together researchers working on generative models of 3D shapes and scenes with researchers and practitioners who can use these generative models to improve embodied vision tasks. For our purposes, we define ``generative model'' to include methods that synthesize geometry unconditionally as well as from sensory inputs (e.g. images), language, or other high-level specifications. Vision tasks that can benefit from such models include scene classification and segmentation, 3D reconstruction, human activity recognition, robotic visual navigation, question answering, and more.
    </p>
  </div>
</div> <br>   

<div class="row" id="cfp">
  <div class="col-xs-12">
    <h2>Call for Papers</h2>
  </div>
</div>
<div class="row">
  <div class="col-xs-12">
    <p>
      <span style="font-weight:500;">Call for papers:</span> We invite novel full papers of 4 to 6 pages (extended abstracts are not allowed) for work on tasks related to data-driven 3D generative modeling or tasks leveraging generated 3D content.
      Paper topics may include but are not limited to:
    </p>
    <ul>
      <li>Generative models for 3D shape and 3D scene synthesis</li>
      <li>Generating 3D shapes and scenes from real world data (images, videos, or scans)</li>
      <li>Representations for 3D shapes and scenes</li>
      <li>Unsupervised feature learning for embodied vision tasks via 3D generative models</li>
      <li>Training data synthesis/augmentation for embodied vision tasks via 3D generative models</li>
    </ul>
    <p>
      <span style="font-weight:500;">Submission:</span> we encourage submissions of up to 6 pages excluding references and acknowledgements.
      The submission should be in the CVPR format.
      Reviewing will be single blind.
      Accepted works will be published in the CVPR 2020 proceedings (online/app, IEEE Xplore, and CVF open access).
      Due to the archival nature of these publications, we are looking for work that has not been published before.
      The submissions will be handled by the <a href='https://cmt3.research.microsoft.com/L3DGM2020'>CMT paper management system</a>. 
      <!--Please submit your paper to the following address by the deadline: <span style="color:#1a1aff;font-weight:400;"><a href="mailto:learn3dgen@gmail.com">learn3dgen@gmail.com</a></span>-->
    </p>
  </div>
</div><br>

<div class="row" id="dates">
  <div class="col-xs-12">
    <h2>Important Dates</h2>
  </div>
</div>

<div class="row">
  <div class="col-xs-12">
    <table class="table table-striped">
      <tbody>
        <tr>
          <td>Paper Submission Deadline</td>
          <td>March 30 2020 - AoE time (UTC -12)</td>
        </tr>
        <tr>
          <td>Notification to Authors</td>
          <td>April 13 2020</td>
        </tr>
        <tr>
          <td>Camera-Ready Deadline</td>
          <td>April 20 2020</td>
        </tr>
        <tr>
          <td>Workshop Date</td>
          <td>June 14 2020</td>
        </tr>
      </tbody>
    </table>
  </div>
</div><br>


<div class="row" id="schedule">
  <div class="col-xs-12">
    <h2>Schedule</h2>
    <p>
      TBA.
    </p>
  </div>
</div>


<br>
<div class="row" id="accepted">
  <div class="col-md-12">
    <h2>Accepted Papers</h2>
    <p>
      TBA.
    </p>
  </div>
</div>


<br>
<div class="row" id="speakers">
  <div class="col-xs-12">
    <h2>Invited Speakers</h2>
  </div>
</div><br>


<!-- 26 -->
<div class="row">
  <div class="col-md-12">
    <a href="https://www.simonsfoundation.org/team/shirley-ho/"><img class="people-pic" style="float:left;margin-right:30px;" src="{{ "/static/img/speakers/shirley.png" | prepend:site.baseurl }}"></a>
    <p>
      <b><a href="https://www.simonsfoundation.org/team/shirley-ho/">Shirley Ho</a></b> is Leader of the Cosmology X Data Science group at the Center for Computational Astrophysics (CCA), Flatiron Institute. Her research interests range from fundamental cosmological measurements to exoplanet statistics to using machine learning to estimate how much dark matter is in the universe. Her goal is to understand the universe’s beginning, evolution and its ultimate fate. Recently she has been developing novel tools using machine learning to solve astrophysical challenges. Shirley plans, builds and analyzes data from a number of astronomical surveys such as Actacama Cosmology Telescope, Euclid, the Large Synoptic Survey Telescope, Simons Observatory, Sloan Digital Sky Survey and the Wide Field Infrared Survey Telescope. She has broad expertise in theory, observation and data science, and her significant experience on machine learning for cosmology will deliver plenty of insights to the CVPR audience. Shirley earned her Ph.D. in astrophysical sciences from Princeton in 2008 and her bachelor’s degrees in computer science and physics from the UC Berkeley in 2004. She was a Chamberlain fellow and a Seaborg fellow at Lawrence Berkeley National Laboratory before joining CMU in 2011 as an assistant professor. She became the Cooper Siegel Career Development Chair Professor and was appointed associate professor with tenure in 2016. She moved to Lawrence Berkeley Lab as a Senior Scientist in 2016. Since 2011, she has been a primary mentor to more than 15 postdoctoral fellows, six graduate students and 14 undergraduates.
    </p>
  </div>
</div><br>

<!-- 24 -->
<div class="row">
  <div class="col-md-12">
    <a href="https://www.linkedin.com/in/courtneymario"><img class="people-pic" style="float:left;margin-right:30px;" src="{{ "/static/img/speakers/courtney.png" | prepend:site.baseurl }}"></a>
    <p>
      <b><a href="https://www.linkedin.com/in/courtneymario">Courtney Mario</a></b> is a Principal Member of the Technical Staff at The Charles Stark Draper Laboratory (Draper Lab) in the Perception and Autonomy Group. Draper Lab is a not-for-profit R&D organization headquartered in Cambridge, Massachusetts. The lab specializes in the design, development, and deployment of advanced technology solutions to problems in space exploration, health care and energy. She is currently a member of the Natural Feature Tracking team for OSIRIS-REx (NASA’s asteroid sample return mission) and is also leading the algorithm development for Draper’s lunar precision landing capability. Prior work has included developing vision-inertial systems for GPS-denied applications for ground vehicles, UAVs, and pedestrians. Courtney has over 9 years of experience in vision navigation systems for GPS-denied environments, and the lessons she has learnt on the challenges of visual navigation in the space environment will be extremely beneficial to the CVPR community. Courtney earned a Bachelor’s degree (graduated Magna Cum Laude) and Master’s degree in mechanical engineering, both from Tufts University.
    </p>
  </div>
</div><br>

<!-- 23 -->
<div class="row">
  <div class="col-md-12">
    <a href="https://www.esa.int/gsp/ACT/team/dario_izzo/"><img class="people-pic" style="float:left;margin-right:30px;" src="{{ "/static/img/speakers/dario.png" | prepend:site.baseurl }}"></a>
    <p>
      <b><a href="https://www.esa.int/gsp/ACT/team/dario_izzo/">Dario Izzo</a></b> is the Scientific Coordinator of the Advanced Concepts Team (ACT) at ESA, where he coordinates all the scientific activities of the ACT and manages the interface of the ACT to the rest of ESA. Dario is a major proponent of AI and champion of deep neural networks to solve space problems. He led studies in interplanetary trajectory design using AI and was responsible for starting the Global Trajectory Optimization Competitions events, the ESA’s Summer of Code in Space, and the Kelvins competition platform which brings together AI and space researchers. At the proposed workshop, Dario will be sharing his expertise and experience on AI algorithms for spacecraft guidance dynamics and control. Dario has published more than 150 papers in journals, conferences and books. In 2013, he received the Humies Gold Medal for the work on grand tours of the galilean moons and, the following year, he won the 8th edition of the Global Trajectory Optimization Competition, organized by NASA/JPL, leading a mixed team of ESA/JAXA scientists. Dario graduated in Aeronautical Engineering from the University Sapienza of Rome in 1999. He later obtained a second master in “Satellite Platforms” at the University of Cranfield in the UK and a Ph.D. in Mathematical Modelling in 2003, at the University Sapienza of Rome where he had the honour to assist Prof. Chiara Valente throughout the classical mechanics and space flight mechanics courses during the academic years 2001-2003.
    </p>
  </div>
</div><br>

<!-- 16 -->
<div class="row">
  <div class="col-md-12">
    <a href="https://www.surrey.ac.uk/people/yang-gao"><img class="people-pic" style="float:left;margin-right:30px;" src="{{ "/static/img/speakers/yang.jpg" | prepend:site.baseurl }}"></a>
    <p>
      <b><a href="https://www.surrey.ac.uk/people/yang-gao">Yang Gao</a></b> is the Professor of Space Autonomous Systems at Surrey Space Centre (SSC) and the Head of the STAR LAB which specializes in visual sensing and navigation in extreme environments. She has 20 years of research experience in developing robotics and autonomous systems, and has been funded by UK Research Innovation, Royal Academy of Engineering, European Commission, European Space Agency, UK Space Agency, as well as industrial companies such as Airbus, NEPTEC, Sellafield and OHB. Yang is also actively involved in the R&D real-world space missions, e.g., ESA's ExoMars, Proba3 and LUCE-ice mapper, UK's MoonLITE/Moonraker, and China's Chang'E 3. Her expertise in solving real-world space visual navigation problems will be of significant interest to the CVPR audience. Yang is an Elected Fellow of Institute of Engineering and Technology (IET) and Royal Aeronautical Society (RAeS). Her research work led to international acclaim, such as International Astronautical Federation’s 3AF Edmond Brun Silver Medal in 2013, COSPAR's Outstanding Paper Award in 2016, First Prize of UKSEDS Lunar Rover Competition in 2017, Finalist of IEEE/ASME's AIM Best Paper Award 2019 and First Prize of Best Poster Award at ICRA 2020 Space Robotics Workshop. Prior to joining SSC in 2004, Yang was an awardee of the prestigious Singapore Millennium Foundation (SMF) Postdoctoral Fellowship and worked on intelligent and autonomous vehicles. She gained the B.Eng. and Ph.D. degrees from the Nanyang Technological University in 2000 and 2003 respectively.
    </p>
  </div>
</div><br>




<div class="row" id="organizers">
  <div class="col-xs-12">
    <h2>Organizers</h2>
  </div>
</div>

<div class="row">

  <div class="col-xs-2">
    <a href="https://cs.adelaide.edu.au/~tjchin">
      <img class="people-pic" src="{{ "/static/img/people/tj.png" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://cs.adelaide.edu.au/~tjchin">Tat-Jun Chin</a>
      <h6>The University of Adelaide</h6>
    </div>
  </div>

  <div class="col-xs-2">
    <a href="https://lucacarlone.mit.edu/">
      <img class="people-pic" src="{{ "/static/img/people/luca.png" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://lucacarlone.mit.edu/">Luca Carlone</a>
      <h6>MIT</h6>
    </div>
  </div>

  <div class="col-xs-2">
    <a href="https://www.linkedin.com/in/marius-klimavi%C4%8Dius-19a6569b/">
      <img class="people-pic" src="{{ "/static/img/people/marius.png" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://www.linkedin.com/in/marius-klimavi%C4%8Dius-19a6569b/">Marius Klimavicius</a>
      <h6>Blackswan Technologies</h6>
    </div>
  </div>

  <div class="col-xs-2">
    <a href="https://staff.qut.edu.au/staff/c.fookes">
      <img class="people-pic" src="{{ "/static/img/people/clinton.png" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://staff.qut.edu.au/staff/c.fookes">Clinton Fookes</a>
      <h6>Queensland University of Technology</h6>
    </div>
  </div>

  <div class="col-xs-2">
    <a href="https://www.esa.int/gsp/ACT/team/marcus_maertens/">
      <img class="people-pic" src="{{ "/static/img/people/marcus.png" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://www.esa.int/gsp/ACT/team/marcus_maertens/">Marcus Märtens</a>
      <h6>ESA</h6>
    </div>
  </div>


  <div class="col-xs-2">
    <a href="https://www.linkedin.com/in/pablo-gomez-ml/">
      <img class="people-pic" src="{{ "/static/img/people/pablo.png" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://www.linkedin.com/in/pablo-gomez-ml/">Pablo Gómez</a>
      <h6>ESA</h6>
    </div>
  </div>
  
  <div class="col-xs-2">
    <a href="https://bochenys.github.io/">
      <img class="people-pic" src="{{ "/static/img/people/bo.jpg" | prepend:site.baseurl }}">
    </a>
    <div class="people-name">
      <a href="https://bochenys.github.io/">Bo Chen</a>
      <h6>The University of Adelaide</h6>
    </div>
  </div>

</div>


<hr>

{% if page.acknowledgements %}
<div class="row">
  <div class="col-xs-12">
    <h2>Acknowledgments</h2>
  </div>
</div>
<a name="/acknowledgements"></a>
<div class="row">
  <div class="col-xs-12">
    <p>
      Thanks to <span style="color:#1a1aff;font-weight:400;"> <a href="https://visualdialog.org/">visualdialog.org</a></span> for the webpage format.
    </p>
  </div>
</div>
{% endif %}

<br>

