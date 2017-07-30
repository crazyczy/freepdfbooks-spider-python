# freepdfbooks-spider-python
最近发现了一个很不错的英文计算机类pdf电子书网站 http://freepdf-books.com ，粗略看了一下大概有几千本吧，于是就想写个爬虫把电子书都爬下来，虽然爬下来也~~不一定~~(一定不)会看，但是不爬一下不就没法享受写爬虫的乐趣了吗😋

如下表格所示，截至目前(2017.7.30)一共有4001本书，总大小26G左右，书的详细页面为 http://freepdf-books.com/download/?file= 后面加上表格中的那个序号id。

|序号|文件名|页码|文件大小|下载次数|
|:----:|:-----|----:|-----:|----:|
|9|Microsoft Exchange Server 2013 Pocket Consultant Databases Services Management|400|6.1 MB|67|
|10|Accessing Data With Microsoft Net Framework|671|4.1 MB|64|
|11|Access 2007 Vba Programming For Dummies|410|4.3 MB|48|
|12|Microsoft Office Access 2003 Step By Step Book|350|8.3 MB|38|
|13|Windows 8 Ebook|147|3.9 MB|28|
|24|Android Developer Tools Essentials|250|16.8 MB|98|
|25|Cracking Drupal|242|3.9 MB|65|
|26|Beginning Programming With Java For Dummies 4th Editionbook|482|10.2 MB|107|
|27|Basic Sensors In iOS|106|4.1 MB|63|
|28|Building Hypermedia Apis With HTML5 And Node|241|6.6 MB|167|
|29|Android Tutorial|216|3.2 MB|72|
|30|Beginning iOS 6 Development|750|15.6 MB|25|
|31|Design And Prototyping For Drupal|168|6.7 MB|56|
|32|CSS - PHP Lecture 4|66|912.3 KB|62|
|33|Build Windows 8 Apps With HTML5 And Javascript|388|17.8 MB|58|
|34|ASP.NET Page Life Cycle - ASP.NET Lecture 3|29|368.9 KB|45|
|35|Android App Mit App Inventor|23|10.8 MB|84|
|36|ASP.NET Database Connectivity - ASP.NET Lecture 6|20|145.5 KB|49|
|37|Beginning iOS Apps With Facebook And Twitter Apis|314|12.2 MB|90|
|38|Building Android Apps With HTML CSS And Javascript|164|3.5 MB|130|
|39|Android Application Development For Dummies|388|7.7 MB|92|
|40|ASP.NET Application Configurations And Server Controls - ASP.NET Lecture 5|21|971.9 KB|43|
|41|Android Application Development Cookbook|410|24.4 MB|94|
|42|Building Android Apps With HTML CSS And Javascript 2nd Edition|176|9.6 MB|187|
|43|Beginning iOS Application Development With HTML And Javascript|436|21.9 MB|76|
|44|Beginning HTML5 Games With Createjs|400|8.1 MB|146|
|45|Advanced Windows Store App Development Using HTML5 And Javascript|435|8.8 MB|72|
|46|Beginning iOS 3d Unreal Games Development|393|10.0 MB|62|
|47|Coffeescript Application Development|258|4.1 MB|26|
|48|Designing Evolvable Web Apis With ASP.NET|536|15.2 MB|112|
|49|Back To Basics Hype Free Principles For Software Developers|41|472.9 KB|58|
|50|Beginning Ejb 3 2nd Edition Book|441|8.6 MB|53|
|51|Beginning iOS 6 Games Development|351|9.7 MB|44|
|52|Beginning iOS 5 Application Development|659|29.2 MB|29|
|53|Beginning Android Web Apps Development|278|10.1 MB|80|
|54|Beginning Responsive Web Design With HTML5 And CSS3|316|12.7 MB|129|
|55|Beginning Java With Websphere|545|21.7 MB|107|
|56|Android Development Busy Coder Guide|731|9.3 MB|88|
|57|Building Powerful And Robust Websites With Drupal 6|380|10.5 MB|31|
|58|Appcelerator Titanium Up And Running|153|5.5 MB|18|
|59|Cisco iOS Xr Fundamentals|504|2.5 MB|45|
|60|ASP.NET Server Controls - ASP.NET Lecture 4|23|678.9 KB|44|
|61|Beginning iOS 5 Development|743|12.6 MB|25|
|62|Beginning Javascript With Dom Scripting And Ajax 2nd Edition Book|377|7.8 MB|130|
|63|Android Studio Development Essentials|65|2.6 MB|283|
|64|ADO.NET - ASP.NET Lecture 7|20|612.5 KB|40|
|65|Building Online Communities With Drupal PHP And WordPress|561|9.1 MB|111|
|66|An Introduction To Network Programming With Java|389|3.1 MB|180|
|67|Beginning Java EE 7|597|8.0 MB|181|
|68|Creating HTML5 Animations With Flash And Wallaby|61|5.9 MB|31|
|69|Android Cookbook|74|7.5 MB|74|
|70|Data Push Apps With HTML5 Sse|221|9.9 MB|50|
|71|Ajax And PHP - PHP Lecture 12|17|748.0 KB|72|
|72|Client Server Web Apps With Javascript And Java|259|7.0 MB|217|
|73|Beginning Webgl For HTML5|348|9.6 MB|30|
|74|Beginning Drupal 7|336|9.1 MB|60|
|75|ASP.NET State Management - ASP.NET Lecture 8|24|256.8 KB|45|
|76|ASP.NET Ajax - ASP.NET Lecture 13|14|172.3 KB|56|
|77|Beginning HTML5 And CSS3|616|17.1 MB|62|
|78|Beginning Programming With Java For Dummies 3rd Edition Book|459|8.9 MB|63|
|79|Android Book|98|2.6 MB|52|
|80|Build Websites With Drupal|209|612.9 KB|46|
|81|Beginning iOS Programming|340|7.8 MB|30|
|82|Designers Guide To Magento|24|579.7 KB|55|
|83|ASP.NET Ajax - ASP.NET Lecture 14|9|144.9 KB|56|
|84|C++ Pointers Arrays Dynamic Memory - C++ Lecture 2|25|265.8 KB|87|
|85|Beginning iOS 5 Games Development|341|8.6 MB|38|
|86|Android Programming|62|1.6 MB|58|
|87|Beginning Phonegap|387|17.3 MB|48|
|88|Android Tutorial Oose|48|2.1 MB|51|
|89|Async Javascript Build More Responsive Apps With Less Code|97|2.1 MB|89|
|90|Beginning iOS 7 Development|705|13.7 MB|27|
|91|Application Development In iOS 7|126|2.4 MB|26|
|92|Android Quick APIs Reference|270|2.9 MB|199|
|93|Android A Programmers Guide|337|5.4 MB|121|
|94|Building Iphone Apps|186|3.9 MB|40|
|95|3d Game Programming For Kids With Javascript|296|4.6 MB|176|
|182|Drupal For Education And E-Learning|400|19.0 MB|95|
|183|Drupal 6 Content Administration|195|8.4 MB|24|
|184|Drupal 7 Module Development|420|5.4 MB|56|
|185|Developing Restful Services With JAX Rs 2.0 Websockets And JSON|128|3.6 MB|61|
|186|Drupal 6 Themes|312|7.7 MB|21|
|187|Developing Windows Store Apps With HTML5 And Javascript|184|4.7 MB|74|
|188|Drupal Creating Blogs Forums Portals And Community Websites|279|5.1 MB|41|
|189|Dreamweaver Cs5.5 Mobile And Web Development With HTML5 CSS3 And Jquery|284|9.3 MB|90|
|190|Drupal 7 Themes|297|4.4 MB|57|
|191|Drupal 6 Attachment Views|300|6.5 MB|22|
|192|Drupal 6 Search Engine Optimization|279|9.3 MB|54|
|193|Drupal 5 Themes Create Drupal Website With CSS|260|6.5 MB|47|
|194|Drupal 7 Book|260|13.8 MB|92|
|195|Drupal 6 Performance Tips|239|6.3 MB|28|
|196|Drupal 7 First Look|288|5.2 MB|45|
|197|Drupal 7 Theming Cookbook|364|5.8 MB|67|
|198|Drupal 6 Panels Cookbook|220|10.3 MB|23|
|199|Drupal E-Commerce With Ubercart 2x|359|15.9 MB|33|
|200|Drupal 7 Business Solutions|379|12.6 MB|68|
|201|Drupal Search Engine Optimization|116|3.3 MB|82|
|202|Drupal 5 Views Recipes|412|6.9 MB|21|
|203|Drupal 6 Site Builder Solutions|336|14.3 MB|30|
|204|Drupal 7 Primer Creating Cms Websites|378|12.3 MB|100|
|205|Drupal 6 Site Blueprints|272|9.8 MB|29|
|206|Drupal Guide To Planning And Building Websites|505|14.3 MB|114|
|207|Documentation For Magento Developers|95|1.4 MB|99|
|208|Drupal 6 Theming Cookbook|384|6.3 MB|23|
|209|Dreamweaver Cs6 Mobile And Web Development With HTML5 CSS3 And Jquery Mobile|268|9.1 MB|130|
|210|Drupal Web Services|320|5.6 MB|46|
|211|Dynamic Web Pages More JavaScript - PHP Lecture 5|23|1.3 MB|58|
|212|Drupal 6 Javascript And Jquery|333|3.9 MB|78|
|213|Drupal For Dummies|387|26.4 MB|676|
|464|Facebook Api Developers Guide|150|2.6 MB|239|
|465|Facebook The Missing Manual 2nd Edition|269|7.5 MB|121|
|466|Facebook All In One For Dummies 2nd Edition|530|18.3 MB|104|
|467|Facebook Marketing All In One For Dummies 3rd Edition|795|26.5 MB|54|
|468|Facebook Marketing For Dummies|315|7.4 MB|53|
|469|Facebook Graph Api Development With Flash|324|6.4 MB|99|
|470|Facebook And Twitter For Seniors For Dummies|338|6.7 MB|108|
|471|Facebook Application Development For Dummies|410|10.5 MB|91|
|480|Microsoft Press Ebook Net Technology Guide For Business Applications|70|4.6 MB|42|
|481|Microsoft Excel 2013 Inside Out|1168|33.1 MB|189|
|482|Microsoft Access 2010 Vba Programming Inside Out|735|24.5 MB|177|
|483|Microsoft Exchange Server 2010 Inside Out|1245|23.0 MB|57|
|484|Microsoft Excel 2013 Step By Step Complete Book|505|9.4 MB|104|
|485|Microsoft Excel 2013 Plain Simple|367|15.6 MB|103|
|486|Microsoft Access 2013 Step By Step|446|7.9 MB|108|
|487|Microsoft Dynamics Gp 2013 Cookbook|348|4.7 MB|39|
|488|Microsoft Ado.Net Entity Framework Step By Step|448|7.9 MB|53|
|489|Microsoft Access 2013 Plain Simple|271|18.8 MB|89|
|500|Magento Ebook Magento Made Easy Vol2|179|4.6 MB|134|
|501|Magento Design Guidelines|26|3.4 MB|57|
|502|Magento Site Performance Optimization|92|1.3 MB|133|
|503|Magento 1.4 Development Cookbook|268|6.0 MB|64|
|504|Magento Facebook Discount|16|2.6 MB|25|
|505|Magento Project Guide|208|5.2 MB|68|
|506|Magento Search Engine Optimization|132|3.2 MB|126|
|507|Magento Ebook Tech|181|2.0 MB|48|
|508|Magento Php Developer Guide|256|3.5 MB|289|
|509|Magento User Guide Community|291|8.9 MB|70|
|510|Magento Beginner Guide 2nd Edition|320|14.6 MB|216|
|511|Magento Reussir Son Site Ecommerce|354|9.2 MB|47|
|512|Magento Mobile How To|78|4.2 MB|108|
|513|Magento Beginners Guide|299|11.4 MB|74|
|514|Magento Ebook Magento Made Easy Vol1|179|4.6 MB|88|
|515|Magento Finalizado|316|8.2 MB|27|
|516|Magento Development Services|1|1.8 MB|35|
|517|Magento 1.4 Themes Design|292|7.9 MB|42|
|518|Magento Extension Developers Guide|80|1.5 MB|79|
|538|Html5 Architecture|78|2.2 MB|42|
|539|Html5 And Css3 2nd Edition|303|7.3 MB|80|
|540|Html Introduction - Php Lecture 2|37|1.4 MB|44|
|541|Hello Html5 And Css3|561|18.8 MB|85|
|542|Html5 Developer Cookbook|472|7.2 MB|36|
|543|Html5 The Missing Manual 2nd Edition|519|21.9 MB|84|
|544|Html5 Game Development For Dummies|387|12.6 MB|306|
|545|Html5 Game Development Insights|457|14.9 MB|58|
|546|Html5 Boilerplate Web Development|174|4.0 MB|36|
|547|Html5 Geolocation|103|2.3 MB|31|
|548|Html5 Step By Step|417|10.3 MB|50|
|549|Html5 Web Application Development By Example|276|3.5 MB|37|
|550|Head First Html5 Programming|610|70.3 MB|374|
|551|Html5 The Missing Manual|449|18.0 MB|41|
|552|Html5 Canvas Cookbook|348|4.1 MB|88|
|553|Html5 And Css3 Responsive Web Design Cookbook|204|5.9 MB|129|
|554|Html5 Video How To|81|2.6 MB|39|
|555|Html5 And Css3|265|3.4 MB|65|
|556|Html5 For Dummies|226|2.3 MB|39|
|557|Html5 Game Programming With Enchant.Js|208|6.0 MB|35|
|558|Html5 Advertising|367|9.9 MB|63|
|559|Html5 Canvas For Dummies|387|20.0 MB|51|
|560|Html5 And Javascript Web Apps|171|9.9 MB|115|
|561|Html5 For Dummies Quick Reference|226|2.3 MB|36|
|562|Html5 For Publishers|57|1.2 MB|31|
|563|Html5 Css3 For The Real World|377|4.6 MB|78|
|564|Html5 And Javascript Projects|446|30.3 MB|143|
|594|Oracle Database 2 Day Dba|292|4.1 MB|40|
|595|Oracle Spatial And Graph Topology Data Model And Network Data Model Graph Developers Guide|404|4.6 MB|45|
|596|Oracle Form Report Developer SQL PLSQL Solved Mcqs|33|650.2 KB|43|
|597|Oracle Database Licensing Information|128|2.0 MB|26|
|598|Oracle Database Migration Assistant For Unicode Release Notes|16|1.4 MB|15|
|599|Oracle 11g Anti Hackers Cookbook|302|3.4 MB|228|
|600|Oracle Database Sql Language Quick Reference|156|1.9 MB|32|
|601|Oracle Spatial And Graph Developers Guide|1040|8.5 MB|21|
|602|Oracle Spatial And Graph RDF Semantic Graph Developers Guide|636|7.5 MB|24|
|603|Oracle Database 2 Day Developers Guide|252|2.4 MB|23|
|604|Oracle Streams Concepts And Administration|796|6.2 MB|25|
|605|Oracle Database Advanced Replication|222|6.9 MB|40|
|606|Oracle Data Mining Users Guide|102|1.7 MB|26|
|607|Oracle Grid Infrastructure Installation Guide For HP UX Itanium|216|2.6 MB|17|
|608|Oracle Database Workspace Manager Developers Guide|362|4.1 MB|20|
|609|Oracle Database JDBC Developers Guide|520|4.2 MB|17|
|610|Oracle Database Installation Guide For IBM AIX On Power Systems|236|2.0 MB|17|
|628|What Is JavaScript Functions|4|574.4 KB|45|
|629|What Is JavaScript Syntax|5|580.8 KB|46|
|630|What Is JavaScript Page Printing|2|555.5 KB|48|
|631|What Is JavaScript Switch Case|3|545.7 KB|43|
|632|What Is JavaScript Page Redirection|4|545.5 KB|43|
|633|What Is JavaScript Operators|7|584.3 KB|42|
|634|What Is JavaScript While Loops|3|567.2 KB|41|
|635|What Is JavaScript Void Keyword|3|544.2 KB|43|
|636|What Is JavaScript Dialog Boxes|3|561.3 KB|42|
|637|What Is JavaScript For In Loop|3|541.5 KB|43|
|638|What Is JavaScript Loop Control|5|596.8 KB|42|
|639|What Is JavaScript If Else Statements|5|585.6 KB|40|
|640|What Is JavaScript Events|6|586.7 KB|42|
|641|What Is JavaScript|5|576.9 KB|45|
|642|What Is JavaScript For Loops|3|559.5 KB|44|
|658|HTML5 Game Development With Gamemaker|364|4.2 MB|37|
|659|HTML5 Game Development With Impactjs|304|3.8 MB|27|
|660|What Is HTML5|18|2.1 MB|25|
|661|HTML5 Up And Running|222|4.0 MB|58|
|662|Using The HTML5 Filesystem API|72|2.7 MB|107|
|663|HTML5 Guidelines For Web Developers|322|7.7 MB|30|
|664|Learn HTML5 By Creating Fun Games|374|3.9 MB|95|
|665|HTML5 Games Development By Example|352|8.1 MB|36|
|666|HTML5 Canvas|643|6.8 MB|28|
|667|HTML5 Geolocation|103|2.3 MB|28|
|668|Learn HTML5 And JavaScript For iOS|287|7.2 MB|96|
|669|HTML5 Enterprise Application Development|332|8.0 MB|61|
|670|Introducing HTML5 Game Development|120|3.5 MB|80|
|671|HTML5 Mobile Development Cookbook|254|3.5 MB|28|
|672|Learning HTML5 Game Programming|254|3.7 MB|28|
|673|HTML5 Pocket Reference 5th Edition|183|2.8 MB|118|
|674|HTML5 And CSS3 Transition Transformation And Animation|136|2.7 MB|116|
|692|Database Management System And Design|9|566.2 KB|29|
|693|Software Engineering Solved Mcqs|16|1.1 MB|106|
|694|Matlab Graphics And Data Visualization Cookbook|284|8.0 MB|159|
|695|Pro HTML5 Programming 2nd Edition|345|6.5 MB|124|
|696|Link Building How To Build Links To Website For Seo Traffic|135|7.1 MB|95|
|697|Building Node Applications With Mongodb And Backbone|203|5.8 MB|31|
|698|Pro HTML5 Performance|285|3.5 MB|37|
|699|CSS Essentials|281|7.3 MB|65|
|700|Seo Certification Study Guide|172|1.5 MB|63|
|701|Concurrent Programming In Mac Os X And iOS|58|1.2 MB|29|
|702|Drupal 6 Social Networking|294|6.7 MB|24|
|703|Computer Architecture And Organization|8|557.9 KB|24|
|704|Computer Networking Mcq|8|558.0 KB|96|
|705|Enabling JavaScript In Browsers|4|569.0 KB|50|
|706|Information System Analysis And Design|11|614.0 KB|17|
|707|What Are JavaScript And Cookies|7|592.4 KB|52|
|708|Microsoft Outlook 2010 A Beginners Guide|24|1.7 MB|31|
|709|PHP And MySQL For Dummies 3rd Edition|455|2.9 MB|73|
|710|iOS Sensor Apps With Arduino|124|5.6 MB|47|
|711|The 36 Hour Course Online Marketing|272|2.6 MB|34|
|712|PHP Programming With Pear XMLl Data Dates Web Services And Web APIs|290|6.3 MB|78|
|713|Data Structures Algorithms Multiple Choice Questions MCQs|16|595.3 KB|76|
|714|Tcl Scripting For Cisco iOS|311|2.9 MB|26|
|715|Operating System Solved Mcqs Part 2|14|605.9 KB|49|
|716|Ccna Mcqs With Answers Set1|23|606.4 KB|62|
|717|MS Outlook Professional Guide To Email Management|14|1.4 MB|41|
|718|MS Word Objective Questions MCQs With Solutions And Explanations|20|616.1 KB|34|
|719|Natural Language Annotation For Machine Learning|97|2.5 MB|63|
|720|Database Design Solved Mcqs Part 2|15|599.4 KB|37|
|721|Professional PHP6|742|7.2 MB|181|
|722|Mobile First Design With HTML5 And CSS3|122|1.9 MB|97|
|723|C++ From The Ground Up Third Edition Book|625|3.7 MB|164|
|724|Basics Of C++ Objective Questions MCQs|23|627.5 KB|31|
|725|Regular Expression Pocket Reference 2nd Edition|128|1.5 MB|74|
|726|Computer Architecture And Organization Mcqs|9|560.3 KB|36|
|727|Solved MCQs On Computer Networking|10|556.1 KB|30|
|728|New Ipad Features In iOS 6 How To|74|4.5 MB|32|
|729|Learn HTML5 And JavaScript For Android|381|6.8 MB|215|
|730|Facebook Marketing Bible 50 Ways To Market Your Brand Company Product Or Service Inside Facebook|252|6.4 MB|112|
|731|Matlab Matrix Algebra|234|1.8 MB|102|
|732|A Guide To Matlab For Beginners And Experienced Users|346|5.7 MB|95|
|733|Automata Theory Solved Mcqs|18|625.2 KB|74|
|734|iOS 7 Game Development|120|2.3 MB|19|
|735|Microsoft Outlook 2010 Calendar Guide|22|1.8 MB|33|
|736|Algorithm Solved Mcqs Part 2|15|604.1 KB|31|
|737|Compiler Design Solved Mcqs Part 2|13|589.3 KB|27|
|738|Object Oriented Programming Solved MCQs Part 2|13|599.3 KB|57|
|739|The Link Building Book|287|5.5 MB|149|
|740|Computer Networks Mcqs|14|579.4 KB|34|
|741|Wireless Home Networking For Dummies|386|6.4 MB|56|
|742|Programming And Data Structure Solved MCQs Part 2|15|1.1 MB|34|
|743|Nhibernate 2 - Rapidly Retrieve Data From Your Database Into .NET Objects|276|7.0 MB|40|
|744|Professional Web Design Smashing Ebook|242|3.1 MB|36|
|745|Paypal APIs Up And Running|124|5.6 MB|95|
|746|50 SEO Tips Free Tips Secrets And Ideas For Search Engine Optimization|106|1.4 MB|83|
|747|Core Data|249|3.8 MB|16|
|748|Computational Colour Science Using Matlab|220|1.8 MB|89|
|749|Computer Graphics Solved Mcqs|15|601.3 KB|28|
|750|Responsive Media In HTML5|128|5.7 MB|50|
|751|Professional CSS For Web Design|459|8.2 MB|63|
|752|Get To The Top On Google|256|2.4 MB|179|
|753|Computer Arithematics Solved Mcqs|31|653.6 KB|31|
|754|iOS And OS X Network Programming Cookbook|300|3.5 MB|67|
|755|Microsoft Outlook 2010 Product Guide|65|740.6 KB|30|
|756|PHP Quick Scripting Reference|120|1.0 MB|104|
|757|Information Systems Software Engineering Mcq Part 2|13|1.0 MB|62|
|758|Search Engine Marketing|288|6.5 MB|95|
|759|Yii Rapid Application Development Hotshot|340|6.9 MB|59|
|760|Quickly Schedule Webex Using Outlook Plug In|14|913.5 KB|26|
|761|PHP Web Scraping|60|1.8 MB|159|
|762|Best Practices For Microsoft Office Outlook 2007|40|1.5 MB|27|
|763|Twitter API Up And Running|416|4.8 MB|125|
|764|Building Mobile Applications Using Kendo UI Mobile And AspNet Web API|256|3.9 MB|82|
|765|Geolocation In iOS|113|5.5 MB|39|
|766|Getting Started With ROO|62|4.7 MB|17|
|767|PHP And Mongodb Web Development|292|5.8 MB|57|
|768|Social Location Marketing|240|6.2 MB|58|
|769|Tutorial PHP MySQL Complet|54|783.7 KB|82|
|770|C++ Concurrency In Action|337|2.7 MB|132|
|771|Managing Your Business With Outlook 2003 For Dummies|362|6.9 MB|19|
|772|iOS Recipes|226|3.4 MB|23|
|773|Programming iOS 4|834|6.5 MB|18|
|774|PHP Solved MCQs|17|612.0 KB|54|
|775|Pc Shortcut Keys Computer Science Important|7|561.5 KB|20|
|776|PHP And MySQL Web Development All In One Desk Reference For Dummies|675|6.6 MB|138|
|777|Microsoft Outlook 2010 User Guide|69|3.9 MB|30|
|778|You Can Program In C++ A Programmer Introduction|391|2.9 MB|82|
|779|Programming Languages MCQs Set|6|552.2 KB|35|
|780|Current Trends And Technologies Solved Mcq|15|597.3 KB|62|
|781|Outlook 2010 Cheat Sheet|17|1.9 MB|26|
|782|iOS Development With Xamarin Cookbook|386|6.0 MB|41|
|783|Computer Arithematics Solved Mcqs|20|618.3 KB|29|
|784|Mac Kung Fu 2nd Edition|461|7.0 MB|49|
|785|JavaScript Placement In HTML File|5|547.4 KB|77|
|786|Microsoft Outlook Shortcut Keys|1|2.3 MB|47|
|787|Learning Opengl ES For iOS|352|5.7 MB|41|
|788|Writing Game Center Apps In iOS|76|1.5 MB|20|
|789|JavaScript Variables And Datatypes|5|578.1 KB|58|
|790|Game And Graphics Programming For iOS And Android With Opengl ES 2|316|6.7 MB|74|
|791|Solved MCQs On Computer Graphics|5|540.5 KB|28|
|792|Introduction To Outlook 2007|34|2.0 MB|18|
|793|Advanced Meta Programming In Classic C++|589|3.4 MB|446|
|794|MS Excel A Set Of Objective Multiple Choice Questions MCQs|32|648.8 KB|81|
|795|Cross Platform Development In C++|575|6.6 MB|147|
|796|Beginning PHP And Postgresql ECommerce|639|7.3 MB|64|
|797|Pro iOS Persistence|376|7.9 MB|31|
|798|Herb Schildts C++ Programming Cookbook|529|6.6 MB|129|
|799|Node Cookbook 2nd Edition|379|3.3 MB|71|
|800|Computer Graphics Solved Mcqs Part 2|15|597.6 KB|27|
|801|Joomla Social Networking With Jomsocial|184|7.5 MB|78|
|802|PHP Manual|723|1.6 MB|43|
|803|Matlab Differential And Integral Calculus|220|5.7 MB|130|
|804|Getting Started With Outlook Express For Windows 2000xp|16|811.9 KB|14|
|805|Artificial Intelligence Solved Mcq Part 2|15|604.9 KB|54|
|806|NodeJS For PHP Developers|286|4.2 MB|119|
|807|Os X And iOS Kernel Programming|473|6.8 MB|30|
|808|Hardening Windows Second Edition|217|5.9 MB|34|
|809|Everything You Know About CSS Is Wrong|132|6.2 MB|88|
|810|iOS Drawing Practical Uikit Solutions|309|6.9 MB|40|
|811|Outlook 2010 Advanced Training Manual|51|5.3 MB|36|
|812|CSS Pocket Reference|250|3.5 MB|50|
|813|Wireless Home Networking For Dummies 2nd Edition|409|7.4 MB|56|
|814|Microsoft Outlook 2007 eMail Training Guide|37|643.9 KB|27|
|815|Microsoft Outlook 2003 Basic Guide|32|2.4 MB|21|
|816|Computer Network Solved Mcqs Part 2|17|626.7 KB|57|
|817|Basic Mcqs Of Computer Science IT For NTS And PSC Test|10|568.7 KB|116|
|818|CSS Mastery Advanced Web Standards Solutions|247|4.0 MB|123|
|819|Interfacing With C++ Programming Real World Applications|492|3.7 MB|150|
|820|Java Networking And Awt Bible|872|3.4 MB|37|
|821|Ajax Solved Mcqs|6|551.2 KB|40|
|822|Authority Seo Domination|46|922.8 KB|67|
|823|Exploring C++ The Programmer Introduction To C++|703|3.0 MB|64|
|824|Getting Started With Intellij Idea|114|1.8 MB|98|
|825|Electronics And Circuit Analysis Using MATLAB|386|4.1 MB|103|
|826|Introduction To MATLAB|354|5.9 MB|57|
|827|Opa Application Development|116|1.2 MB|13|
|828|PHP The Good Parts|176|3.9 MB|105|
|829|Core C++ A Software Engineering Approach|1189|6.6 MB|171|
|830|MS DOS Objective Mcqs With Solutions And Explanations|21|620.9 KB|35|
|831|Getting Started With Beautiful Soup|130|2.4 MB|15|
|832|The PHP Anthology Volume Ii Applications|412|3.9 MB|49|
|833|Home Networking For Dummies 3rd Edition|410|7.0 MB|27|
|834|Hacking And Securing iOS Applications|356|6.4 MB|292|
|835|Magento PHP Developers Guide|256|3.6 MB|74|
|836|Computational Statistics Handbook With Matlab|585|3.9 MB|93|
|837|How To Convert Outlook Email Folder Into A Single Pdf Document|15|1.1 MB|44|
|838|Advanced Mathematics And Mechanics Applications Using Matlab 3rd Edition|665|7.3 MB|72|
|839|Building Polyfills|169|6.9 MB|15|
|840|PHP And Script Aculo Us Web 2 Application Interfaces|263|6.5 MB|35|
|841|Mongodb And PHP|76|7.3 MB|61|
|842|Mac Os X Snow Leopard Pocket Guide|233|3.8 MB|26|
|843|Loop Shaping Robust Control|278|2.7 MB|34|
|844|Outlooksync For Ms Outlook 2007 2010 2013|66|1.8 MB|27|
|845|Digital Systems Solved Mcqs Part 2|13|594.5 KB|30|
|846|iOS SDK Development|286|7.5 MB|27|
|847|Programming PHP 3rd Edition|540|7.6 MB|151|
|848|Mac Kung Fu|318|6.1 MB|35|
|849|MS Access Objective Questions MCQs|37|668.4 KB|36|
|850|Test Driven iOS Development|244|3.6 MB|37|
|851|Learning PHP And Mysql 2nd Edition|430|7.6 MB|129|
|852|Discrete Mathematical Structures Solved Mcqs Part2|13|595.3 KB|24|
|853|Expert C++ CLI Net For Visual C++ Programmers|337|1.9 MB|72|
|854|Essential Matlab For Engineers And Scientists|449|4.1 MB|123|
|855|Discrete Structure Solved Mcqs|11|581.5 KB|130|
|856|Pro PHP MVC|479|2.9 MB|194|
|857|Google Maps Api 2nd Edition Book|76|2.0 MB|81|
|858|Computer Fundamentals Mcqs|74|755.9 KB|95|
|859|C++ Programming Program Design Including Data Structures|1617|9.2 MB|169|
|860|Test iOS Apps With UI Automation|217|6.0 MB|53|
|861|Rails For PHP Developers|409|7.2 MB|61|
|862|Matlab Control Systems Engineering|170|6.8 MB|126|
|863|Migration To HTML5 And CSS3 How To|68|1.4 MB|63|
|864|Web Technologies Solved MCQ Part 2|14|595.5 KB|74|
|865|Programming HTML5 Applications|141|3.4 MB|42|
|866|Beginning JavaScript And CSS Development With Jquery|532|8.4 MB|175|
|867|Algorithm Collections For Digital Signal Processing Applications Using Matlab|199|4.0 MB|111|
|868|PHP Web Services|117|6.2 MB|68|
|869|Link Research Tools Google Penguin 3 Book|22|1.6 MB|86|
|870|Applied Statistics Using Spss Statistica Matlab And R|520|7.3 MB|82|
|871|Applied Numerical Methods Using Matlab|520|3.7 MB|80|
|872|Wireless Home Networking For Dummies 3rd Edition|410|7.5 MB|89|
|873|Data Structures And Program Design In C++|734|6.9 MB|85|
|874|Home Networking For Dummies 4th Edition|362|7.8 MB|41|
|875|Learn Sprite Kit For iOS Game Development|243|7.0 MB|121|
|876|Microsoft Outlook 2010 The Essentials Training User Guide|35|5.3 MB|38|
|877|Configuring Outlook 2007 For Windows Xp|29|2.0 MB|19|
|878|Mechanics Of Composite Materials With Matlab|336|2.6 MB|48|
|879|Metro Revealed Building Windows 8 Apps With HTML5 And JavaScript|103|1.2 MB|48|
|880|Getting Started With Mule Cloud Connect|116|6.7 MB|11|
|881|Advanced Java Networking|363|1.8 MB|46|
|882|Solved MCQs On SQL|11|559.9 KB|77|
|883|Solved MCQs On Data Structures And Algorithms|12|562.8 KB|141|
|884|Opencms 7 Development|288|6.5 MB|18|
|885|Microsoft Outlook Center For Teaching And Learning|27|1.6 MB|33|
|886|Link Building Domination Dominate Search Engines And Get Google Ranking|51|1.1 MB|102|
|887|Pro PHP Programming|433|6.8 MB|104|
|888|The Definitive Guide To HTML5 Websocket|200|5.2 MB|89|
|889|Information Technology Solved Mcqs|9|571.9 KB|119|
|890|Theory Of Computation Solved MCQ Part 2|16|1.1 MB|55|
|891|Plug In PHP 100 Power Solutions|383|7.2 MB|82|
|1124|Object Oriented Programming Using C++ Classes Contd - C++ Lecture 5|8|559.4 KB|47|
|1126|Oracle Database Sample Schemas|52|1.8 MB|34|
|1128|The Art of SEO|602|11.7 MB|40|
|1130|Oracle Database Guard Concepts And Administration|396|4.5 MB|45|
|1132|Oracle Database Sqlj Developer Guide|504|4.2 MB|20|
|1134|Oracle Label Security Administrator Guide|334|4.4 MB|20|
|1136|Oracle Text Application Developer Guide|256|4.2 MB|22|
|1139|50 Android Hacks|218|3.0 MB|552|
|1141|8 In 1 Tips For WordPress Security - Their Issues and Their Solutions|6|976.5 KB|165|
|1143|A Newbies Guide To Apple Watch|95|2.6 MB|25|
|1145|Advance Praise for Black Faces in White Places|289|2.3 MB|32|
|1147|Agile in a Flash|114|1,020.6 KB|16|
|1149|An Introduction to Machine Learning|296|3.1 MB|48|
|1151|Android 4 New Features for Application Development|166|2.3 MB|54|
|1153|Android 6 Essentials - Design Build Create Application Using Android 6|266|2.6 MB|175|
|1155|Android Essentials|118|1.2 MB|82|
|1157|Android Fragmentation Management How to|66|1.9 MB|47|
|1159|Android Fragmentation Management How-to|66|2.0 MB|61|
|1161|Android Fragments - Harness the Power of Fragments to Build Pro Level Android UIs|131|1.7 MB|61|
|1163|Android SQLite Database Tutorial|11|844.8 KB|125|
|1165|Android Studio Application Development|110|1.8 MB|149|
|1167|Ansible for DevOps|316|3.3 MB|1652|
|1169|Apache Cookbook 2nd Edition|308|2.7 MB|166|
|1171|Apache Kafka - Consumers Using Practical Hands-On Examples|88|2.1 MB|91|
|1173|Apache The Definitive Guide 2nd Edition|388|2.2 MB|50|
|1175|Apache ZooKeeper Essentials|169|2.5 MB|184|
|1177|APIs A Strategy Guide|148|3.4 MB|206|
|1179|Application Security for the Android Platform|112|906.6 KB|93|
|1181|Arduino Android Bluetooth|4|671.2 KB|329|
|1183|AutoIt v3 Your Quick Guide|56|956.6 KB|75|
|1185|Automating Microsoft Azure with PowerShell|157|3.2 MB|511|
|1187|Bayesian Networks With Examples in R|239|2.4 MB|71|
|1189|Beautiful Security - Leading Security Expert Explain How They Think|302|2.8 MB|285|
|1191|Building Great Software Engineering Teams - Recruiting, Hiring and Managing Team from Startup to Success|154|1.6 MB|105|
|1193|Building Mobile Applications with Java|84|3.1 MB|135|
|1195|Building on Sugar CRM|80|3.0 MB|91|
|1197|Building UIs with Wijmo|116|2.7 MB|19|
|1199|CCNP Routing and Switching Quick Reference Book|313|2.1 MB|45|
|1201|CCNP SWITCH Portable Command Guide|210|2.1 MB|55|
|1203|Chef Infrastructure Automation Cookbook|276|2.7 MB|89|
|1205|Cloud Architecture Patterns|182|2.2 MB|44|
|1207|Communication Network|198|1.2 MB|44|
|1209|Complexity Management with the K-Method|112|2.2 MB|14|
|1211|CompTIA Aplus 220-801 and 220-802 Cert Guide 3rd Edition Book|174|1.6 MB|43|
|1213|Computing- A Historical and Technical Perspective|340|2.7 MB|51|
|1215|Cracking, Patching - Secugenius Security Solutions Reverse Engineering|25|2.8 MB|338|
|1217|Crackproof Your Software - The Best Ways to Protect Your Software Against Crackers|170|3.4 MB|99|
|1219|Creating HTML5 Animations with Flash and Wallaby|62|2.4 MB|122|
|1221|CRM Fundamentals|244|2.0 MB|84|
|1223|Customizing Chef GET TING THE MOST OUT OF YOUR|387|3.0 MB|27|
|1225|Cyber Security Policy Guidebook|288|3.2 MB|315|
|1227|Cyber Threat- How to Manage the Growing Risk of Cyber Attacks|227|1.6 MB|299|
|1229|Cybersecurity for Executives A Practical Guide|412|2.6 MB|324|
|1231|Cyberspace and Cybersecurity|230|3.1 MB|265|
|1233|Decide to Play Great Poker|500|3.2 MB|32|
|1235|Desenvolvimento de Jogos para Android - Explore sua imaginacao com o framework Cocos2D|177|2.8 MB|190|
|1237|Designing the Internet of Things|338|2.3 MB|43|
|1239|Developing Android Applications with Adobe AIR|303|3.1 MB|57|
|1241|Different Rewrite Methods Available With Mod Rewrite For Blacklisting|13|1.6 MB|12|
|1243|Digital Signage Template|5|984.9 KB|12|
|1245|Disassembling Code IDA Pro and SoftICE|363|2.8 MB|23|
|1247|Distributed Embedded Controller Development with Petri Nets|90|2.5 MB|17|
|1249|DNS and BIND on IPv6 - Networking Book|44|1.1 MB|75|
|1251|Executing Temporal Logic Programs|125|932.7 KB|14|
|1253|Game Developers Guide to Cybiko|419|2.1 MB|42|
|1255|Getting Started with Mule Cloud Connect|116|2.3 MB|44|
|1257|Getting Started with OpenShift|105|2.0 MB|43|
|1259|Getting Started with SOQL|130|2.6 MB|25|
|1261|Google Power Search|72|2.9 MB|170|
|1263|Gradle for Android - Automate the build process for your Android projects with Gradle|172|2.8 MB|100|
|1265|Group Search Optimization for Applications in Structural Design|257|3.4 MB|12|
|1267|Hackers - Heroes Of The Computer Revolution|520|2.7 MB|452|
|1269|Hacking Basic Security - Penetration Testing and How to Hack|55|900.1 KB|507|
|1271|Hello, Android 3rd Edition|302|3.1 MB|54|
|1273|Home Automation with Intel Galileo|188|1.9 MB|42|
|1275|Home Computing Weekly Technology Magazine 030|56|2.5 MB|12|
|1277|Home Computing Weekly Technology Magazine 036|72|3.2 MB|9|
|1279|Home Computing Weekly Technology Magazine 037|56|2.7 MB|14|
|1281|Home Computing Weekly Technology Magazine 038|64|2.7 MB|13|
|1283|Home Computing Weekly Technology Magazine 039|64|2.7 MB|10|
|1285|Home Computing Weekly Technology Magazine 041|72|3.1 MB|9|
|1287|Home Computing Weekly Technology Magazine 042|72|3.2 MB|9|
|1289|Home Computing Weekly Technology Magazine 045|56|2.7 MB|9|
|1291|Home Computing Weekly Technology Magazine 046|56|2.5 MB|9|
|1293|Home Computing Weekly Technology Magazine 047|56|2.5 MB|10|
|1295|Home Computing Weekly Technology Magazine 048|56|2.5 MB|9|
|1297|Home Computing Weekly Technology Magazine 054|56|2.6 MB|9|
|1299|Home Computing Weekly Technology Magazine 057|56|2.6 MB|9|
|1301|Home Computing Weekly Technology Magazine 058|56|2.6 MB|9|
|1303|Home Computing Weekly Technology Magazine 064|56|2.6 MB|10|
|1305|Home Computing Weekly Technology Magazine 065|56|2.5 MB|9|
|1307|Home Computing Weekly Technology Magazine 093|64|2.7 MB|10|
|1309|Homeworld Primas Official Strategy Guide|168|2.4 MB|20|
|1311|How To Easily Root An Android Device|3|878.8 KB|84|
|1313|HSPA Performance and Evolution|286|3.2 MB|12|
|1315|HTML and XHTML Pocket Reference 4th Edition|192|1.5 MB|102|
|1317|HTML5 for Web Designers|96|1.1 MB|171|
|1319|Hyper-V Server Virtualization Starter|59|2.6 MB|29|
|1321|IBM Rational ClearCase 7.0|361|2.6 MB|12|
|1323|Implementing Cloud Storage with OpenStack Swift|140|2.1 MB|62|
|1325|Implementing NetScaler VPX|136|3.2 MB|71|
|1327|Instant Flask Web Development|78|1.3 MB|87|
|1329|Instant Kali Linux - A Quick Guide To Learn The Most Widely Used Operating System By Network Security Professionals|68|3.4 MB|385|
|1331|Intel Trusted Execution Technology for Server Platforms|149|2.7 MB|17|
|1333|Intelligent Systems Approximation by Artificial Neural Networks|113|1.2 MB|55|
|1335|Internet of Things with the Arduino Yun|112|2.5 MB|412|
|1337|Internetworking Technologies|219|771.6 KB|42|
|1339|Introduction to Concurrency Theory Transition Systems and CCS|341|3.3 MB|32|
|1341|Introduction To HTML and CSS|155|3.1 MB|104|
|1343|Laravel Application Development Cookbook|272|2.6 MB|772|
|1345|Learning Apache Kafka, 2nd Edition|210|2.3 MB|522|
|1347|Learning Google Guice|132|1.2 MB|84|
|1349|Learning NServiceBus, 2nd Edition|204|2.9 MB|96|
|1351|Learning Redis - Design efficient web and business solutions with Redis|318|2.7 MB|55|
|1353|Learning WebRTC|186|2.3 MB|131|
|1355|Learning Windows Azure Mobile Services for Windows 8 and Windows Phone 8|124|2.1 MB|86|
|1357|Linux The Ultimate Step by Step Guide to Quickly and Easily Learning Linux|168|3.0 MB|209|
|1359|MAC Protocols for Cyber Physical Systems|98|3.1 MB|170|
|1361|Make Getting Started with Sensors - Measured Arduino|140|3.1 MB|545|
|1363|Making Friends on the Fly- Advances in Ad Hoc Teamwork|157|3.0 MB|18|
|1365|Manage Partitions with GParted How-to|86|3.2 MB|31|
|1367|Managing Infrastructure with Puppet|46|1.1 MB|38|
|1369|Managing Risk and Information Security|143|2.2 MB|181|
|1371|Managing Windows Servers with Chef|110|1.6 MB|62|
|1373|Mapping and Visualization with SuperCollider|222|3.0 MB|53|
|1375|Mastering Puppet - Pull the strings of Puppet to configure|280|2.6 MB|109|
|1377|MCSD Certification Toolkit|650|2.3 MB|17|
|1379|Microsoft Dynamics AX 2012 R3 Security|106|2.9 MB|95|
|1381|Microsoft Dynamics AX 2012 Services|196|3.3 MB|52|
|1383|Microsoft Visual C# .Net And Microsoft Visual Studio .Net Version 3.0.0|60|1.4 MB|112|
|1385|MIPS Assembly Language Programming using QtSpim|165|2.9 MB|19|
|1387|Mobile Web Browsing Using the Cloud|57|1.0 MB|29|
|1389|Monitoring with Opsview|158|2.6 MB|22|
|1391|MOS 2013 Study Guide for Microsoft Word|186|3.0 MB|59|
|1393|Munin Plugin Starter|62|1.8 MB|15|
|1395|Net Works Case Studies in Web Art and Design|261|3.3 MB|18|
|1397|Network Backup with Bacula How To|55|1.3 MB|74|
|1399|NETWORK CALCULUS - A Theory of Deterministic Queuing Systems for the Internet|263|2.3 MB|38|
|1401|Network Security with OpenSSL|338|2.1 MB|251|
|1403|Nginx HTTP Server 2nd Edition|319|3.0 MB|72|
|1405|Nginx Module Extension|129|1.4 MB|40|
|1407|Object Oriented Technology|222|1.5 MB|140|
|1409|OCA Oracle Certified Associate Java SE 8 Programmer Study Guide Exam 1Z0 808|435|2.9 MB|5015|
|1411|OpenStack Swift|336|3.3 MB|68|
|1413|OpenVZ Essentials Create and administer virtualized|110|2.9 MB|19|
|1415|Oracle Certified Associate Java SE 7 Programmer Study Guide|332|2.6 MB|88|
|1417|Oracle Certified Professional Java SE 7 Programmer Exams 1Z0 804 and 1Z0 805|644|3.1 MB|156|
|1419|PCs For Dummies Quick Reference 3rd Edition|230|2.6 MB|18|
|1421|Phparchitects Zend PHP 5 Certification Study Guide Book|278|2.1 MB|83|
|1423|Practical Reverse Engineering|383|3.1 MB|64|
|1425|Pro Puppet Maximize and customize Puppets|332|3.4 MB|36|
|1427|Programming Arduino with LabVIEW|102|2.7 MB|393|
|1429|Programming for PaaS|143|1.7 MB|20|
|1431|Programming Google App Engine|392|3.2 MB|96|
|1433|Programming Google Glass|128|2.8 MB|53|
|1435|Protect Your Privacy - Importance of Data Privacy|48|957.3 KB|20|
|1437|Protecting Your Mobile App IP The Mini Missing Manual|109|1,017.4 KB|34|
|1439|Proxmox High Availability|258|3.3 MB|69|
|1441|Puppet 3 Beginners Guide|205|2.3 MB|199|
|1443|Puppet Cookbook 3rd Edition|336|2.5 MB|196|
|1445|Puppet Essentials - Using the power of Puppet to manage IT infrastructure|234|2.7 MB|72|
|1447|Puppet Types and Providers|92|2.4 MB|35|
|1449|Resilience and Reliability on AWS|162|2.8 MB|38|
|1451|Rethinking Enterprise Storage A Hybrid Cloud Model|120|2.1 MB|18|
|1453|Sass for Web Designers|94|1.8 MB|117|
|1455|Scalability Rules|273|2.2 MB|33|
|1457|Scrum and Xp from the Trenches 2nd Edition|183|3.2 MB|213|
|1459|Scrum Shortcuts without Cutting Corners|205|2.5 MB|80|
|1461|Securing Ajax Applications|251|2.7 MB|71|
|1463|Security and Privacy for Mobile Healthcare Networks|130|2.1 MB|196|
|1465|Security Metrics - Replacing Fear,Uncertainty and Doubt|335|3.1 MB|233|
|1467|Seeking Chances- From Biased Rationality to Distributed Cognition|182|1.7 MB|14|
|1469|Service Virtualization|148|3.3 MB|22|
|1471|SOA Governance - The key to successful SOA adoption|229|1.8 MB|23|
|1473|SOA in Practice - Service Oriented Architecture|344|3.0 MB|25|
|1475|SOA Made Simple - Service Oriented Architecture|292|3.4 MB|63|
|1477|SOA Using Java  Web Services|605|2.9 MB|137|
|1479|Software Testing - Concepts and Operations|401|3.3 MB|154|
|1481|Spring for Android Starter - Leverage Spring for Android to create RESTful and OAuth Android apps|73|2.2 MB|43|
|1483|Spring for Android Starter Instant Spring for Android Starter|73|2.2 MB|85|
|1485|Systematic Program Design|258|1.8 MB|42|
|1487|Test Driven Infrastructure with Chef 2nd Edition|308|2.6 MB|53|
|1489|Test Driven Infrastructure with Chef|88|1.1 MB|14|
|1491|The Apache Modules Book|590|3.0 MB|51|
|1493|The Art of Computer programming|140|1.7 MB|39|
|1495|The Business of Android Apps Development, 2nd Edition|162|2.9 MB|66|
|1497|The Definitive Guide to Apache mod rewrite|159|1.3 MB|83|
|1499|The Definitive Guide to SugarCRM|275|3.0 MB|85|
|1501|The Developers Guide to Social Programming|335|3.2 MB|50|
|1503|The Entrepreneurs Strategy Guide - Ten Keys for Achieving Marketplace Leadership and Operational Excellence|321|2.0 MB|41|
|1505|The Fundamentals of Network Security|219|3.3 MB|99|
|1507|The Intelligent Web|320|2.1 MB|19|
|1509|The Leprechauns of Software Engineering|183|1.9 MB|102|
|1511|The Managers Guide to Web Application Security|221|2.0 MB|227|
|1513|The Myths of Security - What the Computer Security Industry|262|2.2 MB|295|
|1515|The Zend PHP Certification Practice Test Book|127|1.4 MB|102|
|1517|Todd Lammles CCNA CCENT IOS Commands Survival Guide|181|1.2 MB|36|
|1519|Web Corpus Construction|147|1.9 MB|98|
|1521|Whats New in Flash Player 11|79|2.6 MB|17|
|1523|Windows 7 Enterprise Desktop Support Technician|138|1.3 MB|50|
|1525|Windows Azure Hybrid Cloud|218|2.8 MB|250|
|1527|Windows Azure Web Sites|115|2.0 MB|257|
|1529|Wireless Communications over MIMO Channels - Networking Book|390|3.4 MB|109|
|1531|Working Together Apart- Collaboration Over the Internet|153|2.2 MB|13|
|1533|Xamarin Mobile Application Development for Android|168|2.8 MB|95|
|1535|Zabbix Cookbook - Over 70 Hands On Recipes To Get Your Infrastructure Up And Running With Zabbix|260|3.3 MB|156|
|1537|ZeroMQ - How To Apply Different Message Patterns|108|1.4 MB|18|
|1539|3G Evolution HSPA and LTE for Mobile Broadband - Networking Book|485|4.0 MB|120|
|1541|A Practical Guide to Networking and Security in iOS 8|127|3.6 MB|70|
|1543|ActionScript 3.0 Cookbook|588|3.6 MB|19|
|1545|Advanced Strategies Primas Official Strategy Guide David Ellis|192|4.0 MB|20|
|1547|Algorithms for Sensor Systems|175|3.4 MB|31|
|1549|Android Application Development with Maven|192|4.3 MB|62|
|1551|Android Application Programming with OpenCV|130|3.7 MB|76|
|1553|Android User Interface Development Beginners Guide|304|3.5 MB|144|
|1555|Ansible Playbook Essentials|168|3.7 MB|213|
|1557|Apache The Definitive Guide 3rd Edition|622|3.7 MB|143|
|1559|Applied Cryptography 2nd Edition|662|3.8 MB|284|
|1561|Automating Microsoft Azure Infrastructure Services|178|3.6 MB|340|
|1563|Beginners Introduction to the Assembly Language of ATMEL AVR Microprocessors|81|2.2 MB|30|
|1565|Beginning the Linux Command Line, 2nd edition|399|4.1 MB|435|
|1567|Big Data and The Internet of Things|207|4.1 MB|62|
|1569|Big Data For Dummies|339|4.0 MB|48|
|1571|Building Web Apps for Google TV|117|4.0 MB|101|
|1573|CCNA Routing and Switching Practice 1001 Questions For Dummies|483|4.0 MB|29|
|1575|Cisco Router Configuration Handbook 2nd Edition - Networking Book|665|3.9 MB|148|
|1577|Code in the Cloud|306|3.4 MB|19|
|1579|Computer Viruses For Dummies|290|3.7 MB|36|
|1581|Dart Cookbooks - Over 110 incredibly recipes to design Dart web client and server applications - Networking Book|346|4.2 MB|54|
|1583|Database Nation - The Death of Privacy in the 21st Century|388|4.0 MB|22|
|1585|Decision Theory with Imperfect Information|467|3.5 MB|23|
|1587|Developing Android Applications with Flex 4.5|112|3.5 MB|56|
|1589|DevOps Troubleshooting Linux Server Best Practices|235|3.7 MB|461|
|1591|Distibuted Systems design and algorithms|323|3.9 MB|22|
|1593|Effective Monitoring and Alerting|164|3.6 MB|88|
|1595|Essential Cyber Security Science|190|3.5 MB|420|
|1597|Essential GWT Building for the Web with Google Web Toolkit 2|344|3.6 MB|118|
|1599|Force.com Tips and Tricks|225|3.7 MB|15|
|1601|Fundamentals of Convolutional Coding|689|4.2 MB|32|
|1603|Fundamentals of Sensor Network Programming - Networking Book|342|3.8 MB|84|
|1605|Game Theory - Strategies Equilibria And Theorems|396|4.0 MB|106|
|1608|Getting Started with BizTalk Services|180|4.1 MB|23|
|1610|Google Compute Engine|246|3.5 MB|175|
|1612|Harnessing Green IT|433|3.7 MB|15|
|1614|Hello Android 3rd Edition|302|3.9 MB|87|
|1616|Home Computing Weekly Technology Magazine 040|84|3.7 MB|11|
|1618|Hyper V Security Secure your Hyper-V hosts and services from intruders and malware|184|4.2 MB|186|
|1620|Identity Theft In Controversy|96|4.1 MB|16|
|1622|Implementing Microsoft Dynamics AX 2012 with Sure Step 2012|234|4.0 MB|41|
|1624|Information Theory and Coding by Example|528|3.9 MB|23|
|1626|Knoppix Hacks, 2nd Edition|422|3.9 MB|165|
|1628|Learn using Superior Tools developed by Superior GMAT Instructors 4th Edition Book|202|3.9 MB|202|
|1630|Learn using Superior Tools developed by Superior GMAT Instructors Guide 6|190|4.3 MB|232|
|1632|Learn using Superior Tools developed by Superior GMAT Instructors|174|3.8 MB|210|
|1634|Learning BeagleBone|206|3.6 MB|23|
|1636|Learning Veeam Backup - Replication for VMware vSphere|110|4.3 MB|40|
|1638|Machine Learning Paradigms- Applications in Recommender Systems|135|4.0 MB|118|
|1640|Mastering SQL Queries for SAP Business One|352|3.6 MB|216|
|1642|Metasploit Penetration Testing Cookbook|269|3.6 MB|50|
|1644|Microsoft Dynamics CRM 2011 Applications MB2-868 Certification Guide|344|3.7 MB|60|
|1646|Microsoft Dynamics CRM 2011 Scripting Cookbook|268|3.5 MB|81|
|1648|Microsoft Forefront UAG Mobile Configuration Starter|86|3.5 MB|27|
|1650|Microsoft Windows Communication Foundation 4.0 Cookbook for Developing SOA Applications|316|3.9 MB|64|
|1652|Model Based Development- Applications|549|4.1 MB|23|
|1654|Nginx HTTP Server - Adopt Nginx for your web applications|348|3.9 MB|49|
|1656|OFDM-Based Broadband Wireless Networks|264|3.9 MB|122|
|1658|OpenStack Operations Guide|329|3.6 MB|64|
|1660|Optimizing and Troubleshooting Hyper-V Networking|132|3.9 MB|91|
|1662|Penetration Testing with the Bash shell|151|3.5 MB|68|
|1664|Perceptual Image Coding with Discrete Cosine Transform|74|2.7 MB|14|
|1666|PGP and GPG - Email for the Practical Paranoid|216|3.6 MB|34|
|1668|PHP and MySQL For Dummies 3rd Edition|455|3.7 MB|101|
|1670|Practical Zendesk Administration, 2nd Edition|195|4.2 MB|18|
|1672|Practical Zendesk Administration|187|3.7 MB|13|
|1674|Primas Official Strategy Guide|183|4.0 MB|18|
|1676|Pro Android Augmented Reality|343|3.7 MB|112|
|1678|Pro Apache, 3rd Edition|903|4.0 MB|141|
|1680|Pro Puppet, 2nd Edition|318|4.3 MB|78|
|1682|Professional Android Wearables|243|4.3 MB|114|
|1684|Programmer introduction to MIPS assembly language|726|3.3 MB|14|
|1686|Programming in C Exam Ref 70 483|377|3.6 MB|33|
|1688|RabbitMQ Essentials - how to utilize RabbitMQ|182|3.8 MB|30|
|1690|Radio Resource Management Strategies in UMTS - Networking Book|364|4.1 MB|39|
|1692|Reverse Engineering Code with IDA Pro|329|4.2 MB|173|
|1694|RFID For Dummies|409|4.1 MB|19|
|1696|Rootkits For Dummies|425|4.0 MB|22|
|1698|Running Mainframe z on Distributed Platforms|276|4.0 MB|13|
|1700|SEO For 2016 - The Complete Do It Yourself SEO Guide|273|3.6 MB|168|
|1702|SharePoint Apps with LightSwitch|78|3.9 MB|40|
|1704|Shipping Greatness learned on the job at Google|224|3.4 MB|124|
|1706|SOA and WS-BPEL - Composing Service Oriented Solutions with PHP and ActiveBPEL|313|3.7 MB|31|
|1708|SOA Approach to Integration|382|4.0 MB|26|
|1710|Softimage Towards a New Theory of the Digital Image|160|4.0 MB|31|
|1712|Surface Computing and Collaborative Analysis Work|170|3.8 MB|18|
|1714|Testing and Validation of Computer Simulation Models|258|3.5 MB|31|
|1716|4G Wireless Video Communications - Networking Book|412|4.8 MB|121|
|1718|A foundation in digital Communication|749|7.5 MB|12|
|1720|A Practical Guide to TPM 2.0|375|4.4 MB|57|
|1722|A Smarter Way to Learn HTML and CSS|322|6.3 MB|590|
|1724|Access Forms And Reports For Dummies|408|7.0 MB|66|
|1726|ACCUMULO - Application Development, Table Design and Best Practices|552|8.2 MB|15|
|1728|Adobe Flash 11 Stage3D Game Programming|412|4.9 MB|68|
|1730|Advanced Android 4 Games|302|6.7 MB|89|
|1732|Advanced Cellular Network Planning and Optimisation|544|6.6 MB|81|
|1734|AdvancED CSS|358|5.0 MB|65|
|1736|Advanced Programming in the UNIX Environment, 3rd Edition|1034|5.3 MB|129|
|1738|Advanced Windows Store App Development Using C#|460|6.6 MB|119|
|1740|Advances in Security of Information and Communication Networks - Networking Book|260|4.6 MB|51|
|1742|Algorithms and Parallel Computing - Networking Book|365|5.5 MB|82|
|1744|An Introduction to Computer Networks|681|6.3 MB|62|
|1746|Android Application Programming with OpenCV 3|190|4.6 MB|166|
|1748|Android Game Programming by Example|389|4.5 MB|215|
|1750|Android Hackers Handbook|577|7.6 MB|1192|
|1752|Android NDK Beginners Guide - Android and inject the power of C and C++ in your applications|436|6.5 MB|113|
|1754|Android NDK Beginners Guide|436|6.5 MB|74|
|1756|Android Phones For Dummies 3rd Edition|446|7.6 MB|844|
|1758|Android Programming Tutorials 3rd Edition|334|5.3 MB|126|
|1760|Android Programming|104|5.7 MB|84|
|1762|Android Security  Attacks and Defenses|272|8.3 MB|83|
|1764|Android Security Internals - An In-Depth Guide To Androids Security Architecture|434|5.9 MB|81|
|1766|Apache OfBiz Cookbook|300|4.9 MB|105|
|1768|Apache Tomcat 7|287|4.4 MB|137|
|1770|Aplus Network Security Exams in a Nutshell|813|4.9 MB|89|
|1772|Appcelerator Titanium Business Application Development Cookbook|329|6.0 MB|11|
|1774|Arduino Android Blueprints|250|4.6 MB|256|
|1776|Arduino Workshop|394|6.8 MB|462|
|1778|Asterisk The Definitive Guide 3rd Edition - Networking Book|725|5.6 MB|76|
|1780|Away3D 3.6 Essentials|400|5.5 MB|20|
|1782|BackTrack 4 Assuring Security by Penetration Testing|392|5.9 MB|216|
|1784|Bayesian Programming|378|5.5 MB|34|
|1786|Beginning Android ADK with Arduino|310|6.9 MB|427|
|1788|Beginning Android Tablet Programming|288|4.9 MB|80|
|1790|Beginning Google Blogger|190|5.1 MB|120|
|1792|Beginning Google Glass Development|358|7.4 MB|59|
|1794|Beginning Google Maps API 3|329|5.4 MB|241|
|1796|Beginning NFC - Introduction to Arduino and NFC|245|5.3 MB|285|
|1798|Beginning SharePoint with Excel|278|5.7 MB|97|
|1800|BlackBerry Enterprise Server 5 Implementation Guide|216|4.9 MB|16|
|1802|Building Android Apps with HTML CSS and JavaScript|182|5.9 MB|198|
|1804|Building Dashboards with Microsoft Dynamics GP 2013 and Excel 2013|268|6.7 MB|78|
|1806|Building Hybrid Android Apps with Java and JavaScript|153|4.4 MB|104|
|1808|Building iPhone and iPad Electronic Projects|332|7.6 MB|88|
|1810|Canvas LMS Course Design|248|5.2 MB|12|
|1812|CCNA Security Portable Command Guide|367|5.2 MB|253|
|1814|CCNA Wireless 640 722 Official Cert Guide|543|7.5 MB|85|
|1816|CCNP Routing and Switching ROUTE 300-101 Official Cert Guide|1012|5.1 MB|414|
|1818|Citrix Access Gateway VPX 5.04 Essentials|234|4.6 MB|51|
|1820|CiviCRM Cookbook Master this web-based constituent relationship|236|6.5 MB|29|
|1822|CiviCRM Cookbook|236|4.5 MB|38|
|1824|Cloud Security and Privacy|336|4.8 MB|279|
|1826|Cognitive Networks Applications and Deployments|496|4.3 MB|62|
|1828|Cognitive Radio Networks - Networking Book|362|6.9 MB|46|
|1830|Communication Systems An Introduction to Signals and Noise in Electrical Communication|954|5.9 MB|35|
|1832|Complex Valued Neural Networks Advances and Applications|302|5.3 MB|38|
|1834|Computer Forensics JumpStart, 2nd Edition|338|5.3 MB|59|
|1836|Computer Graphics and Geometric Modeling|970|5.2 MB|82|
|1838|Concepts of Programming Languages 10th Edition|816|4.4 MB|31|
|1840|Configuration Guide for Asterisk PBX|372|8.1 MB|42|
|1842|Crafting the InfoSec Playbook - Networking Book|275|4.5 MB|89|
|1844|CSS for Print Designers|178|6.5 MB|58|
|1846|Cuckoo Malware Analysis - Analyze malware using Cuckoo Sandbox|142|6.6 MB|46|
|1848|Cyber Security - Analytics Technology and Automation|268|4.7 MB|341|
|1850|Data Analysis For Network Cyber-Security|200|5.4 MB|469|
|1852|Data Storage Networking Real World Skills for the CompTIA Storage Certification and Beyond|602|5.7 MB|132|
|1854|Data-Driven Security|354|8.0 MB|234|
|1856|Designing Socially Embedded Technologies in the Real World|431|6.5 MB|37|
|1858|Developing AR Games for iOS and Android|130|6.4 MB|89|
|1860|Developing ASP.NET MVC 4 Web Applications Exam Ref 70 486|386|6.9 MB|286|
|1862|Disaster Recovery using VMware vSphere Replication and vCenter Site Recovery Manager|162|4.4 MB|120|
|1864|Disgaea Hour of Darkness 2nd Edition|98|7.4 MB|10|
|1866|Distributed Networks- Intelligence, Security and Applications|399|8.1 MB|121|
|1868|End to End Network Security|469|7.5 MB|102|
|1870|Energy Efficient Servers|347|4.7 MB|18|
|1872|Engineering Secure Software and Systems|238|4.0 MB|55|
|1874|Essentials of Developing Windows Store Apps Using C#|444|7.1 MB|110|
|1876|Ethernet The Definitive Guide, 2nd Edition|508|6.1 MB|82|
|1878|Exam 70-516 Accessing Data with Microsoft NET Framework 4|671|5.3 MB|121|
|1880|Exam 70-687 Configuring Windows 8 Lab Manual|218|4.9 MB|33|
|1882|Exam Ref 70 532 Developing Microsoft Azure Solutions|432|8.0 MB|2779|
|1884|Exam Ref 70-533 Implementing Microsoft Azure Infrastructure Solutions|400|7.8 MB|3284|
|1886|excel 2010 just the steps for dummies|244|7.6 MB|46|
|1888|Excel VBA Programming For Dummies 3rd Edition|411|6.0 MB|353|
|1890|Expert Android - Programming 3D Graphics with OpenGL|425|4.7 MB|159|
|1892|Facebook Graph API Development with Flash|324|6.4 MB|122|
|1894|Fire Tablets For Dummies|292|7.3 MB|13|
|1896|Flash Development for Android Cookbook|372|8.2 MB|88|
|1898|Flash Game Development by Example|328|4.5 MB|58|
|1900|Flash Multiplayer Virtual Worlds|412|7.9 MB|31|
|1902|Force.com Development Blueprints|350|8.3 MB|29|
|1904|Formal Methods for Web Services|345|7.2 MB|34|
|1906|Formalizing Data-Centric Web Services|136|5.2 MB|33|
|1908|Foundations of Statistical Algorithms|495|4.5 MB|31|
|1910|Game and Graphics Programming for iOS and Android with OpenGL ES 2.0|316|6.2 MB|220|
|1912|Game User Experience Evaluation|286|5.1 MB|107|
|1914|Gephi Cookbook - Over 90 Hands On Recipes To Master The Art Of Network Analysis And Visualization With Gephi|296|7.7 MB|77|
|1916|Getting Started with Dynamics NAV 2013 Application Development|230|8.2 MB|55|
|1918|GlassFish Security - Secure your GlassFish installation Web applications EJB applications Application client module and Web Services using Java EE and GlassFish|296|5.1 MB|72|
|1920|Google Analytics|218|6.8 MB|155|
|1922|Google Android - crie aplicacoes para celulares e tablets|309|5.8 MB|130|
|1924|Google Glass For Dummies|243|7.2 MB|73|
|1926|Google Script Enterprise Application Essentials|214|4.9 MB|149|
|1928|Google Visualization API Essentials|252|6.2 MB|162|
|1930|GSM Architecture, Protocols and Services 3rd Edition - Networking Book|327|7.2 MB|239|
|1932|GSM GPRS and EDGE Performance Evolution Towards 3GUMTS|656|8.1 MB|22|
|1934|Hacking Exposed Linux Security Secrets And Solutions, 3rd Edition|649|7.4 MB|395|
|1936|Hacking Exposed Malware and Rootkits Security Secrets And Solutions|401|7.0 MB|348|
|1938|Hacking Exposed Mobile Security Secrets And Solutions|320|5.7 MB|681|
|1940|Hacking Exposed Web 2.0 Security Secrets And Solutions|290|5.5 MB|334|
|1942|Hacking Exposed Web Applications, 3rd Edition|481|6.4 MB|478|
|1944|Hacking Exposed Windows Security Secrets And Solutions, 3rd Edition|482|5.7 MB|497|
|1946|Hacking The Art Of Exploitation 2nd Edition|492|6.4 MB|569|
|1948|Hacking VoIP - An Introduction to VoIP Security|236|5.2 MB|302|
|1950|HL7 for BizTalk|196|5.5 MB|23|
|1952|Home Networking Bible, 2nd Edition - Networking Book|766|8.2 MB|67|
|1954|HTML5 CSS3 For The Real World 2nd Edition|395|4.4 MB|353|
|1956|HTML5 Game Development by Example Beginners Guide Second Edition|354|7.1 MB|160|
|1958|HTML5 Game Development from the Ground Up with Construct 2|260|6.8 MB|321|
|1960|HTML5 Mastery Semantics Standards and Styling|309|4.7 MB|190|
|1962|Hyper-V Network Virtualization Cookbook - Networking Book|228|7.4 MB|119|
|1964|IBM Lotus Domino - Classic Web Application Development Techniques|335|5.4 MB|30|
|1966|Implementing SugarCRM|328|7.8 MB|61|
|1968|Implementing VMware vCenter Server - Networking Book|325|6.6 MB|107|
|1970|Intel Galileo Blueprints|192|5.0 MB|37|
|1972|Intelligent Systems- A Modern Approach|456|6.4 MB|69|
|1974|Introducing HTML5 2nd Edition|314|4.5 MB|192|
|1976|Introducing Windows Azure Hdinsight|130|6.0 MB|160|
|1978|Io Programmo Magzine 101|97|7.8 MB|13|
|1980|Io Programmo Magzine 102|94|7.7 MB|11|
|1982|Io Programmo Magzine 103|96|7.8 MB|13|
|1984|Io Programmo Magzine 107|97|7.5 MB|12|
|1986|Io Programmo Magzine 117|104|8.0 MB|12|
|1988|Io Programmo Magzine 119|104|8.0 MB|12|
|1990|Io Programmo Magzine 91|118|8.1 MB|11|
|1992|IT Architecture For Dummies|364|5.8 MB|247|
|1994|Java Programming Fundamentals|756|4.6 MB|116|
|1996|Juniper QFX5100 Series|309|5.2 MB|40|
|1998|Junos Security|848|6.9 MB|150|
|2000|Kali Linux Network Scanning Cookbook|452|5.6 MB|379|
|2002|Laptops For Dummies Quick Reference 2nd Edition|242|4.6 MB|14|
|2004|Latest Advances in Inductive Logic Programming|264|4.4 MB|28|
|2006|Lean Websites|267|7.2 MB|87|
|2008|Learning Android Application Programming for the Kindle Fire|353|5.6 MB|54|
|2010|Learning AWS, Design, Build And Deploy Applications Using AWS - Networking Book|237|7.2 MB|265|
|2012|Learning Lonic - Build real-time and hybrid mobile applications with Ionic|388|7.0 MB|87|
|2014|Learning Nagios 4 - Learn how to set up Nagios 4|400|5.1 MB|74|
|2016|Learning NServiceBus Sagas|214|6.4 MB|20|
|2018|Learning Pentesting for Android Devices|154|4.4 MB|148|
|2020|Learning Python Network Programming|320|6.1 MB|629|
|2022|Learning The Vi And Vim Editors, 7th Edition|494|4.9 MB|64|
|2024|Learning YARN - management and big data processing using YARN|278|5.3 MB|133|
|2026|Linear and Nonlinear Programming 4 edition|547|4.8 MB|25|
|2028|Linux and Solaris Recipes for Oracle DBAs|485|6.7 MB|194|
|2030|Linux The Complete Reference, Sixth Edition|866|5.8 MB|213|
|2032|Local Online Advertising For Dummies|394|5.6 MB|17|
|2034|Lumion3D Best Practices|166|6.1 MB|22|
|2036|Machine Learning with R|396|5.8 MB|54|
|2038|Managing Derivatives Contracts|476|4.6 MB|36|
|2040|MANHATTAN GMAT Fractions Decimals and Percents GMAT Strategy Guide|120|4.7 MB|299|
|2042|MANHATTAN GMAT Geometry GMAT Strategy Guide2|163|6.1 MB|278|
|2044|MANHATTAN GMAT Geometry GMAT Strategy Guide3|131|5.4 MB|308|
|2046|MANHATTAN GMAT Geometry GMAT Strategy Guide4|119|4.8 MB|336|
|2048|Mastering System Center Configuration Manager|278|5.2 MB|167|
|2050|Mastering vRealize Operations Manager|272|8.3 MB|173|
|2052|MCTS Microsoft Silverlight 4 Development 70 506 Certification Guide|291|5.2 MB|18|
|2054|Meta-Learning in Decision Tree Induction|349|5.4 MB|40|
|2056|Microsoft Dynamics CRM Customization Essentials|238|5.5 MB|110|
|2058|Microsoft Dynamics NAV Administration|208|5.2 MB|177|
|2060|Microsoft Dynamics NAV Financial Management|134|4.3 MB|152|
|2062|Microsoft Exchange Server 2013 PowerShell Cookbook, 2nd Edition|504|4.6 MB|172|
|2064|Microsoft Lync 2013 Unified Communications|224|5.6 MB|70|
|2066|Microsoft SharePoint - Building Office 2007 Solutions in C# 2005|540|6.7 MB|78|
|2068|Microsoft SharePoint 2007 for Office 2007 Users|457|7.1 MB|26|
|2070|Microsoft SharePoint 2010 Enterprise Applications on Windows Phone 7|252|6.7 MB|40|
|2072|Microsoft System Center 2012 Orchestrator Cookbook - Networking Book|318|6.9 MB|98|
|2074|Microsoft System Center Data Protection Manager 2012 SP1|328|7.3 MB|48|
|2076|Mobile Radio Network Design in the VHF and UHF Bands - Networking Book|423|5.8 MB|65|
|2078|Mobile Web Design For Dummies|388|5.3 MB|132|
|2080|Modelling and Dimensioning of Mobile Wireless Networks - Networking Book|342|6.7 MB|120|
|2082|Modelling the Wireless Propagation Channel - Networking Book|272|7.0 MB|77|
|2084|Modulation and Coding Techniques in Wireless Communications - Networking Book|682|8.5 MB|207|
|2086|Monitoring with Ganglia|254|4.4 MB|62|
|2088|Mule in Action, 2nd Edition|432|6.4 MB|13|
|2090|Nagios Core Administration Cookbook|366|4.5 MB|66|
|2092|Network Security Assessment, 2nd Edition|506|5.0 MB|123|
|2094|Network Security Hacks - Tips And Tools For Protecting Your Privacy, 2nd Edition|480|5.9 MB|504|
|2096|Networking Fundamentals Exam 98 366|209|5.0 MB|109|
|2098|Networks of Networks The Last Frontier of Complexity|342|7.0 MB|52|
|2100|Nginx 1 Web Server Implementation Cookbook|236|5.0 MB|86|
|2102|NX-OS and Cisco Nexus Switching|481|5.7 MB|72|
|2104|OCA OCP Java SE 7 Programmer I and II Study Guide Exams 1Z0 803 and 1Z0 804|1094|6.7 MB|117|
|2106|Official ISC Guide to the CISSP ISSMP CBK Second Edition Book|449|6.7 MB|53|
|2108|Official ISC2 Guide To The CISSP ISSMP CBK - Information Systems Security Management Professional, Second Edition|449|7.0 MB|322|
|2110|OpenGL ES 2 for Android, A Quick Start Guide|330|4.7 MB|145|
|2112|OpenStack Cloud Computing Cookbook|318|4.9 MB|46|
|2114|OpenVPN 2 Cookbook 100 Recipes For OpenVPN 2 Network - Networking Book|356|6.6 MB|145|
|2116|Optimization for Computer Vision|266|7.0 MB|35|
|2118|Optimizing and Troubleshooting Hyper-V Storage|152|5.7 MB|30|
|2120|Oracle Application Express 4.0 with Ext JS|393|5.4 MB|29|
|2122|Oracle CRM On Demand Administration Essentials|304|6.3 MB|46|
|2124|Oracle Siebel CRM 8 Developer-s Handbook|577|7.4 MB|53|
|2126|Oracle Siebel CRM 8 Installation and Management|572|7.0 MB|79|
|2128|Oracle SOA Suite 11g Administrator-s Handbook|380|7.1 MB|37|
|2130|PowerPoint 2003 Just the Steps For Dummies|219|7.7 MB|20|
|2132|Practical Enterprise Software Development Techniques|223|5.5 MB|121|
|2134|Practical SharePoint 2010 Branding and Customization|363|6.8 MB|46|
|2136|Primer to Analysis of Genomic Data Using R|283|6.1 MB|158|
|2138|Privacy in a Digital Networked World|419|6.0 MB|52|
|2140|Pro Android Cplusplus with the NDK|404|4.9 MB|45|
|2142|Pro Android C++ with the NDK|404|4.8 MB|258|
|2144|Pro Android Python with SL4A - Build Android Apps with Python|296|6.3 MB|131|
|2146|Pro CSS Techniques|405|6.5 MB|70|
|2148|Pro SharePoint 2010 Search|517|8.3 MB|35|
|2150|Pro SharePoint Disaster Recovery and High Availability, 2nd Edition|252|7.6 MB|77|
|2152|Pro SharePoint with jQuery|268|6.9 MB|169|
|2154|Pro Vim|406|6.9 MB|203|
|2156|Professional NFC Application Development for Android|316|5.0 MB|74|
|2158|Programmers Guide to Java SCJP Certification 3rd Edition|1090|6.6 MB|71|
|2160|Programming Android 2nd Edition|564|6.2 MB|107|
|2162|Programming The Z80 3rd Edition|630|5.8 MB|19|
|2164|Programming WCF Services, 3rd Edition|910|6.2 MB|34|
|2166|Project 2010 For Dummies|436|7.1 MB|25|
|2168|QoS and QoE Management in UMTS Cellular Systems - Networking Book|483|6.7 MB|75|
|2170|Quick Guide to Flash Catalyst|74|4.9 MB|17|
|2172|RabbitMQ in Action|314|5.1 MB|36|
|2174|Railway Infrastructure Security|255|6.6 MB|155|
|2176|Rethinking the Internet of Things - Networking Book|185|4.7 MB|94|
|2178|Robotics- A Project Based Approach|236|4.9 MB|70|
|2180|Router Security Strategies Securing IP Network Traffic Planes - Networking Book|673|4.5 MB|121|
|2182|Salesforce CRM Admin Cookbook|266|7.6 MB|72|
|2184|Sams Teach Yourself Android Application Development in 24 Hours 2nd Edition|512|6.2 MB|335|
|2186|Sams Teach Yourself Samsung Galaxy Tab in 10 Minutes|180|6.0 MB|31|
|2188|Sams Teach Yourself SAP in 24 Hours, 4th Edition|430|4.9 MB|177|
|2190|SCBCD Exam Study Kit Java Business Component Developer Certification for EJB|485|5.3 MB|74|
|2192|Scene Vision- Making Sense of What We See|331|5.9 MB|18|
|2194|Securing VoIP Networks|384|4.4 MB|284|
|2196|Security Monitoring|248|4.6 MB|299|
|2198|Security Planning - An Applied Approach|294|5.4 MB|320|
|2200|sendmail, 4th Edition|1310|7.1 MB|32|
|2202|Service Quality of Cloud Based Applications|340|6.5 MB|16|
|2204|SharePoint 2010 at Work|266|8.1 MB|43|
|2206|SharePoint 2010 Six in One|597|6.5 MB|33|
|2208|Signaling System 7, 6th Edition - Networking Book|670|5.4 MB|51|
|2210|SimCity 4 - Primas Official Strategy Guide|481|8.0 MB|30|
|2212|SIP Trunking - Networking Book|352|4.9 MB|100|
|2214|SOA Governance in Action|312|5.9 MB|20|
|2216|SOA Patterns - Service Oriented Architecture|296|4.9 MB|18|
|2218|Software Engineering Design Theory and Practice|365|4.9 MB|140|
|2220|Software Networks - Virtualization SDN 5G Security|262|6.8 MB|176|
|2222|Spring Security 3 - Secure Web Applications Against Malicious Intruders With This Easy To Follow Practical Guide|420|6.0 MB|40|
|2224|Statistical Computing in Cplusplus and R|553|4.7 MB|31|
|2226|Sugar CRM Developers Manual Customize and extend SugarCRM|296|6.7 MB|84|
|2228|Surface For Dummies|259|7.7 MB|14|
|2230|Systematic CRM Plan Using CiviCRM|464|5.6 MB|30|
|2232|The ActionScript 3.0 Quick Reference Guide|493|5.3 MB|23|
|2234|The Antivirus Hackers Handbook|384|6.1 MB|443|
|2236|The Art of Assembly Language|1426|5.6 MB|23|
|2238|The Compleat Strategyst Being a Primer on the Theory of Games of Strategy|286|6.4 MB|83|
|2240|The Game Artists Guide to Maya|238|5.4 MB|88|
|2242|The Grid Core Technologies|452|4.3 MB|40|
|2244|The Handbook of Ad Hoc Wireless Networks|559|8.1 MB|109|
|2246|THE IDA PRO BOOK - The Unofficial Guide to the World Most Popular Disassembler, 2nd Edition|676|8.3 MB|136|
|2248|The Official Ubuntu Book, 6th edition|424|5.4 MB|125|
|2250|The Second Internet Reinventing Computer Networking with IPv6|306|4.8 MB|75|
|2252|The Ultimate HTML Reference|545|5.1 MB|86|
|2254|Theoretical Foundations of Artificial General Intelligence|331|7.0 MB|26|
|2256|Threat Modeling Designing for Security|626|5.7 MB|49|
|2258|Tomcat The Definitive Guide, 2nd Edition|496|4.7 MB|206|
|2260|Transnational Security|358|3.6 MB|236|
|2262|TrixBox Made Easy - Step By Step Guide for VoIP System - Networking Book|166|3.6 MB|57|
|2264|Twitter Application Development For Dummies|459|6.1 MB|21|
|2266|Ubuntu Hacks|348|4.1 MB|290|
|2268|Ubuntu Kung Fu|369|5.7 MB|70|
|2270|Ubuntu Powerful Hacks and Customizations|531|5.7 MB|458|
|2272|Ubuntu Unleashed 2010 Edition, 5th Edition|863|7.6 MB|29|
|2274|Ubuntu Unleashed 2012 Edition|858|6.8 MB|40|
|2276|Ultra Low Bit Rate Speech Coding|156|4.1 MB|19|
|2278|Unboxing Android USB|189|3.9 MB|116|
|2280|Understanding TCPIP - A clear and comprehensive guide to TCP IP protocols|478|6.6 MB|235|
|2282|Using CiviCRM - CRM plan for your organization using CiviCRM|464|6.4 MB|56|
|2284|Using Google App Engine|264|5.2 MB|108|
|2286|Validation of Evolving Software|216|6.0 MB|50|
|2288|Visual Cryptography for Image Processing and Security|177|5.2 MB|217|
|2290|VMware vCenter Operations Manager Essentials|246|8.3 MB|32|
|2292|VMware Workstation - No Experience Necessary|136|3.5 MB|58|
|2294|VoIP For Dummies|313|6.1 MB|29|
|2296|WCDMA for UMTS HSPA Evolution and LTE|574|7.7 MB|72|
|2298|Web Development Recipes|339|4.6 MB|69|
|2300|Web Scraping with Python|255|3.6 MB|466|
|2302|Web Security Testing Cookbook|314|3.8 MB|103|
|2304|Webmin Administrators Cookbook|376|7.4 MB|29|
|2306|What Is Computer Science|244|4.7 MB|33|
|2308|Windows For Tablets For Dummies|320|8.0 MB|22|
|2310|Windows Phone 8 Game Development - Networking Book|499|6.3 MB|58|
|2312|Wireless Communications, 2nd Edition|884|7.2 MB|107|
|2314|Wireless Home Networking For Dummies|387|5.3 MB|136|
|2316|WordPress and Flash 10x Cookbook|268|4.3 MB|85|
|2318|WordPress Search Engine Optimization 2nd Edition|318|4.6 MB|265|
|2320|Working with Microsoft FAST Search Server 2010 for SharePoint|482|7.0 MB|35|
|2322|Zabbix Network Monitoring Essentials|231|3.6 MB|275|
|2324|Zend PHP 5 Certification Study Guide 3rd Edition Book|363|3.9 MB|348|
|2326|Zenoss Core 3.x Network and System Monitoring|312|8.2 MB|56|
|2328|ZooKeeper and Programming with ZooKeeper|238|3.9 MB|25|
|2330|4g Deployment Strategies And Operational Implications Book|177|3.4 MB|17|
|2332|802 Wireless Networks The Definitive Guide 2nd Edition - Networking Book|730|8.2 MB|75|
|2334|802.11ac A Survival Guide|149|3.3 MB|85|
|2336|A Development And Deployment Perspective - IMS Book|318|3.7 MB|26|
|2338|Access 2010 All in One For Dummies|795|14.8 MB|74|
|2340|ActionScript for Flash MX The Definitive Guide 2nd Edition|1382|11.8 MB|20|
|2342|Administering Windows Server 2012|716|33.1 MB|70|
|2344|Adobe Flash Professional CS6 Digital Classroom|482|18.1 MB|117|
|2346|Adobe Muse Classroom In A Book|273|18.6 MB|304|
|2348|Adobe Photoshop Cs6 Bible|1122|66.1 MB|255|
|2350|Adobe Photoshop Cs6 Digital Classroom|450|20.6 MB|211|
|2352|Advanced Numerical Simulation Methods- From Cad Data Directly To Simulation Results|330|5.9 MB|29|
|2354|Advanced Penetration Testing for Highly Secured Environments|414|10.7 MB|79|
|2356|Advanced Solutions of Microsoft SharePoint Server 2013 Exam Ref 70-332|397|8.0 MB|69|
|2358|Advanced Wireless Networks Cognitive Cooperative Opportunistic 4G Technology 2nd Edition|894|11.6 MB|183|
|2360|Advertising on Google The High Performance Cookbook|372|10.8 MB|99|
|2362|Alcatel Lucent Scalable IP Networks SelfStudy Guide|723|11.1 MB|41|
|2364|American McGees Alice Primas|281|10.9 MB|10|
|2366|An Introduction To Lte 2nd Edition Book|487|3.3 MB|38|
|2368|An Introduction to Regression Graphics|265|9.4 MB|61|
|2370|Analytics For Managerial Decision Making Book|36|4.2 MB|11|
|2372|Andengine For Android Game Development Cookbook|380|5.4 MB|192|
|2374|Android Application Development For Dummies 2nd Edition|411|11.2 MB|115|
|2376|Android Application Development for the Intel Platform|508|19.6 MB|54|
|2378|Android Apps for Absolute Beginners 3rd Edition|696|44.9 MB|214|
|2380|Android Apps for Absolute Beginners|336|31.9 MB|83|
|2382|Android Arcade Game App|99|1.5 MB|172|
|2384|Android Game Recipes|240|2.1 MB|160|
|2386|Android in Action 3rd Edition|662|10.5 MB|111|
|2388|Android on x86 - An Introduction to Optimizing for Intel Architecture|375|10.4 MB|69|
|2390|Android Programming - The Big Nerd Ranch Guide|625|13.1 MB|583|
|2392|Android Studio New Media Fundamentals|152|10.5 MB|208|
|2394|Android Tablets For Dummies 3rd Edition|355|10.7 MB|103|
|2396|Ansible Up And Running Book|332|3.1 MB|301|
|2398|App Inventor Create Your Own Android Apps|385|10.5 MB|119|
|2400|Apple Laptops Mac Book 13-inch Late 2006 Mid 2007 Service Manual|360|43.6 MB|21|
|2402|Arcgis For Desktop Cookbook|372|11.8 MB|34|
|2404|Architecting Mobile Solutions for the Enterprise|472|9.9 MB|39|
|2406|Architecting The Cloud Book|351|2.0 MB|34|
|2408|Art Of Seo Third Edition Ebook|690|24.0 MB|51|
|2410|Asterisk Cookbook|66|1.2 MB|42|
|2412|Asterisk The Definitive Guide 4th Edition|845|8.4 MB|136|
|2414|Asynchronous Control for Networked Systems - Networking Book|349|10.4 MB|63|
|2416|Attract Visitors To Your Site The Mini Missing Manual|60|1.0 MB|21|
|2418|Autocad 2013 For Dummies|595|18.8 MB|140|
|2420|Autocad Civil 3d 2013 Essentials|402|14.4 MB|89|
|2422|Autodesk Drainage Design For Infraworks 360 Essentials 2nd Edition Book|123|7.2 MB|19|
|2424|Autodesk Roadway Design For Infraworks 360 Essentials 2nd Edition Book|124|6.8 MB|39|
|2426|Balsamiq Wireframes Quickstart Guide Book|142|5.4 MB|58|
|2428|Bandit Algorithms For Website Optimization Ebook|87|2.1 MB|49|
|2430|Basics Of Accounting Information Processing Book|51|4.5 MB|11|
|2432|Basics Of Matlab And Beyond|205|3.6 MB|122|
|2434|Beginning .Net Game Programming In VB.Net|430|4.8 MB|69|
|2436|Beginning Android 4 Application Development|564|19.4 MB|115|
|2438|Beginning Android C++ Game Development|302|4.9 MB|414|
|2440|Beginning Android Tablet Application Development|290|17.5 MB|76|
|2442|Beginning Game Development With Python And Pygame|342|3.8 MB|205|
|2444|Beginning Google Sketchup for 3D Printing|329|15.5 MB|81|
|2446|Beginning PowerShell for SharePoint 2013|222|10.6 MB|244|
|2448|Beginning Python Games Development 2nd Edition Ebook|290|5.0 MB|173|
|2450|Beginning SharePoint 2013 Development|460|15.5 MB|88|
|2452|Beginning SUSE Linux - From Novice to Professional|512|9.5 MB|103|
|2454|Beginning Swift Games Development For Ios|259|7.2 MB|176|
|2456|Beginning Ubuntu Linux, 5th Edition|665|14.5 MB|222|
|2458|BizTalk 2010 Recipes|610|9.7 MB|11|
|2460|Blueprints Visual Scripting For Unreal Engine|188|6.3 MB|459|
|2462|Broadband Optical Access Networks - Networking Book|301|10.8 MB|96|
|2464|Build An Html5 Game - A Developers Guide With Css And Javascript|220|5.6 MB|262|
|2466|Build Ios Games With Sprite Kit|211|5.9 MB|44|
|2468|Building A Virtualized Network Solution|136|6.5 MB|65|
|2470|Building Android Games With Cocos2d-x|160|3.1 MB|95|
|2472|Building Applications With Ibeacon Book|80|2.4 MB|19|
|2474|Building Internet Firewalls 2nd Edition Book|542|4.9 MB|112|
|2476|Building Javascript Games|422|6.8 MB|79|
|2478|Building Minecraft Server Modifications|142|2.8 MB|19|
|2480|Building Web Sites All in One Desk Reference For Dummies|795|28.0 MB|69|
|2482|Building Your First Mobile Game Using Xna 4.0|159|2.7 MB|44|
|2484|Business Economics And Finance With Matlab Gis And Simulation Models|457|4.0 MB|79|
|2486|C Programming for Arduino|512|9.2 MB|439|
|2488|Camel Intelligent Networks For The Gsm Gprs And Umts Network Book|428|3.2 MB|150|
|2490|CCENT CCNA ICND1 100-101 Official Cert Guide|1188|45.6 MB|104|
|2492|CCIE Routing and Switching v5 Official Cert Guide Volume 1 - 5th Edition|957|10.0 MB|84|
|2494|CCNP Routing and Switching SWITCH 300-115 Official Cert Guide|578|6.9 MB|315|
|2496|Cellular Authentication For Mobile And Internet Services Book|218|2.3 MB|26|
|2498|Cellular Mobile Radio Systems|211|10.9 MB|30|
|2500|Cellular Technologies For Emerging Markets Book|330|4.0 MB|15|
|2502|Cisco Firewalls Networking|912|10.4 MB|97|
|2504|Cisco Ios Xr Fundamentals Book|504|3.0 MB|42|
|2506|Cisco Routers For The Desperate 2nd Edition Book|148|2.8 MB|24|
|2508|Cisco TelePresence Fundamentals - Networking Book|620|9.4 MB|76|
|2510|Cisco Unified Contact Center Enterprise -UCCE|306|5.0 MB|18|
|2512|Cloud Computing For Dummies Book|339|5.1 MB|56|
|2514|Cloud Portability And Interoperability - Springerbriefs In Computer Science|132|6.5 MB|20|
|2516|Cocos2d Game Development Blueprints|548|6.6 MB|70|
|2518|Cocos2d-X Beginners Guide 2nd Edition Ebook|270|4.2 MB|40|
|2520|Cocos2d-X Game Development Essentials|137|3.9 MB|60|
|2522|Coding Theory Book|355|2.4 MB|35|
|2524|Collaborative Web Hosting Challenges And Research Directions|63|3.4 MB|31|
|2526|Computational Intelligence in Digital and Network Designs and Applications|360|9.6 MB|70|
|2528|Computer Network Software And Hardware Engineering With Applications|601|4.5 MB|133|
|2530|Computer Networking - Principles Protocols and Practice|282|9.6 MB|125|
|2532|Computer Networks 5th Edition Book|962|7.6 MB|173|
|2534|Computer Networks Performance and Quality Services|595|10.6 MB|75|
|2536|Computer Security ESORICS 2013 - 18th European Symposium on Research in Computer Security|810|8.0 MB|194|
|2538|Computing Networks Book|253|3.2 MB|60|
|2540|Concise Guide To Databases|316|8.6 MB|81|
|2542|Configuring Advanced Windows Server 2012 R2 Services|385|8.1 MB|66|
|2544|Configuring Cisco Unified Communications Manager and Unity Connection, 2nd Edition|699|14.2 MB|85|
|2546|Core And Metro Networks|513|8.4 MB|67|
|2548|Coreos Essentials|132|3.9 MB|72|
|2550|C++ Game Development Primer|85|1.6 MB|342|
|2552|Create Stunning Html Email That Just Works|168|4.6 MB|48|
|2554|Creating Games With Cocos2d For Iphone 2|388|4.9 MB|47|
|2556|Cryptography And Network Security 5th Edition Book|900|7.5 MB|536|
|2558|CSS Web Design For Dummies|385|12.6 MB|104|
|2560|CSS3 Solutions|333|8.5 MB|286|
|2562|Custom SharePoint Solutions with HTML and JavaScript|240|9.1 MB|333|
|2564|Customer Analytics For Dummies Ebook|340|5.1 MB|16|
|2566|Data Communications and Networking 3rd Edition|1171|11.3 MB|211|
|2568|Deploying Cisco Wide Area Application Services 2nd Edition - Networking Book|649|10.7 MB|88|
|2570|Designing and Implementing IPMPLS-Based Ethernet Layer 2 VPN Services|987|12.9 MB|24|
|2572|Designing Games Ebook|415|5.3 MB|73|
|2574|Designing Large Scale Lans Book|256|2.7 MB|44|
|2576|Developing Microsoft SharePoint Applications Using Windows Azure|337|11.8 MB|167|
|2578|Developing Mobile Games With Moai Sdk|136|4.2 MB|33|
|2580|Device-Free Object Tracking Using Passive Tags|66|3.4 MB|19|
|2582|Directx 11.1 Game Programming|146|3.0 MB|103|
|2584|Distributed Graph Algorithms For Computer Networks|328|3.9 MB|94|
|2586|Docker Cookbook|359|5.2 MB|497|
|2588|Droid 2 The Missing Manual|396|14.2 MB|10|
|2590|Droid 3 For Dummies|371|9.7 MB|8|
|2592|E-Mail Marketing For Dummies Ebook|570|9.1 MB|17|
|2594|Edge For Mobile Internet|241|3.4 MB|26|
|2596|Efficient Methods For Wcdma Radio Network Planning And Optimization Book|187|2.8 MB|31|
|2598|Elastix Unified Communications Server Cookbook|348|10.3 MB|279|
|2600|Embed With Games|128|2.6 MB|97|
|2602|Emerging Wireless Multimedia Services And Technologies|454|5.3 MB|65|
|2604|End to End Quality of Service over Cellular Networks|317|9.8 MB|61|
|2606|Energy Efficient Distributed Computing Systems|830|6.7 MB|16|
|2608|Essential Snmp 2nd Edition Book|462|4.8 MB|113|
|2610|Ethernet Switches Book|80|2.1 MB|24|
|2612|Ethernet The Definitive Guide Book|527|8.7 MB|54|
|2614|Exam Ref 70-410 Installing and Configuring Windows Server 2012|400|8.5 MB|69|
|2616|Exam Ref 70-413 Designing and Implementing a Server Infrastructure 2nd Edition Book|352|80.6 MB|65|
|2618|excel 2010 all in one for dummies|795|15.0 MB|97|
|2620|Excel 2010 For Dummies|412|11.1 MB|54|
|2622|Excel Formulas and Functions For Dummies 3rd Edition ebooks|410|10.3 MB|84|
|2624|Excel Formulas and Functions For Dummies 3rd Edition|410|10.3 MB|142|
|2626|Expert Oracle Application Express|611|18.8 MB|42|
|2628|Expert SharePoint 2010 Practices|751|23.0 MB|50|
|2630|Facebook Marketing All In One For Dummies 3rd Edition Ebook|795|27.4 MB|275|
|2632|Facebook Marketing For Dummies Ebook|315|7.3 MB|69|
|2634|Femtocells Design And Application Book|272|2.7 MB|21|
|2636|Femtocells Technologies And Deployment Book|329|2.9 MB|31|
|2638|Firewalls For Dummies Book|433|6.3 MB|31|
|2640|Flash and PHP Bible|529|9.5 MB|57|
|2642|Flash Catalyst CS5 Bible|603|17.2 MB|19|
|2644|Flash CS6 The Missing Manual|850|29.1 MB|28|
|2648|Flash Professional CS5 and Flash Catalyst CS5 For Dummies|489|11.1 MB|25|
|2650|Foundations Of Network Optimization And Games|512|6.9 MB|58|
|2652|Foundations Of Semantic Web Technologies|456|4.2 MB|328|
|2654|Free Radius Book|344|3.7 MB|30|
|2656|Freeswitch 1.2|428|4.0 MB|84|
|2658|Freeswitch 1dot6 Cookbook Book|190|2.7 MB|131|
|2660|Freeswitch Cookbook|150|1.8 MB|33|
|2662|Fundamentals Of Wimax|478|4.1 MB|16|
|2664|Game Ai Pro- Collected Wisdom Of Game Ai Professionals|612|6.8 MB|641|
|2666|Game Development With Slimdx|150|2.7 MB|58|
|2668|Game Development With Three.Js|118|2.6 MB|174|
|2670|Game Invaders Ebook|235|2.9 MB|62|
|2672|Game Theory An Introduction|417|4.0 MB|109|
|2674|Gamemaker Essentials Ebook|154|2.8 MB|99|
|2676|Games of Strategy 2nd Edition|675|14.0 MB|163|
|2678|Gamesalad Essentials|154|6.9 MB|77|
|2680|Getting Started With Citrix Cloudportal Book|128|2.4 MB|13|
|2682|Getting Started With Citrix VDI In A Box Book|86|1.5 MB|17|
|2684|Getting Started With C++ Audio Programming For Game Development|117|2.2 MB|265|
|2686|Getting Started with CSS|563|9.4 MB|56|
|2688|Getting Started With Unity 5|184|5.8 MB|575|
|2690|Gns3 Network Simulation Guide Book|155|2.9 MB|151|
|2692|God of War III Guide|221|11.7 MB|14|
|2694|Google Advertising Tools 2nd Edition Ebook|432|13.1 MB|115|
|2696|Google Adwords For Dummies 2nd Edition Ebook|437|9.0 MB|160|
|2698|Google Analytics 3rd Edition Ebook|435|10.0 MB|242|
|2700|Google Maps JavaScript API Cookbook|316|8.4 MB|321|
|2702|Google SketchUp 7 For Dummies|461|12.4 MB|107|
|2704|Google SketchUp Cookbook|384|11.3 MB|115|
|2706|Gpgpu Programming For Games And Science|464|5.2 MB|173|
|2708|GPRS Networks|299|4.3 MB|58|
|2710|Grand Theft Auto San Andreas|29|9.6 MB|12|
|2712|Gray Hat Hacking - The Ethical Hackers Handbook Third Edition|721|12.5 MB|724|
|2714|Grome Terrain Modeling With Ogre3d Udk And Unity 3d|162|7.0 MB|132|
|2716|GSM System Engineering|472|13.0 MB|103|
|2718|Gsmedge Evolution And Performance Book|516|6.3 MB|11|
|2720|Guide To Computer Network Security 3rd Edition|550|8.6 MB|140|
|2722|Hacking Exposed Computer Forensics, 2nd Edition|545|11.6 MB|501|
|2724|Hacking Exposed Security Secrets And Solutions, 6th Edition|720|11.7 MB|392|
|2726|Hacking Exposed Wireless Security Secrets And Solutions, 2nd Edition|513|10.1 MB|641|
|2728|Hacking For Dummies, 4th Edition|411|10.2 MB|602|
|2730|Hadoop Backup And Recovery Solutions Book|206|2.9 MB|198|
|2732|Hardening Azure Applications|195|5.0 MB|155|
|2734|Head First Android Development|532|34.6 MB|103|
|2736|Home Networking All in One Desk Reference For Dummies|723|9.6 MB|64|
|2738|How to Do Everything - Ubuntu|350|8.8 MB|100|
|2740|How To Make A Website And An Ebook Income|136|3.5 MB|83|
|2742|Hsdpahsupa For Umts|259|4.4 MB|10|
|2746|HTML XHTML CSS For Dummies 7th Edition|420|14.6 MB|615|
|2748|Html5 Game Development With Gamemaker|364|5.3 MB|134|
|2750|Html5 Game Development With Impactjs|304|4.3 MB|124|
|2752|Html5 Game Engines App Development And Distribution|212|2.0 MB|224|
|2754|Html5 Game Programming With Enchant.Js|208|6.6 MB|116|
|2756|HTML5 Games Most Wanted - Build the Best HTML5 Games|278|12.5 MB|174|
|2758|HTTP Succinctly Book|55|1.7 MB|131|
|2760|HTTP The Definitive Guide|658|7.3 MB|77|
|2762|IBM Lotus Notes and Domino 8.5.1|336|10.0 MB|16|
|2764|IBM Lotus Notes and Domino 8.5.3 Upgraders Guide|364|11.8 MB|17|
|2766|iLife 04 All-in-One Desk Reference For Dummies|603|12.0 MB|9|
|2768|Implementing Cisco Unified Communications Voice over IP and QoS Cvoice 4th Edition|730|9.8 MB|87|
|2770|Implementing SSL TLS Using Cryptography And PKI|697|4.4 MB|398|
|2772|Inbound Marketing Get Found Using Google Social Media And Blogs|236|15.2 MB|260|
|2774|Independent Guide To Ebay 2016|148|10.6 MB|79|
|2776|InDesign CS3 For Dummies|435|8.0 MB|49|
|2778|Indoor Radio Planning|344|5.7 MB|45|
|2780|Information Security The Complete Reference 2nd Edition|897|12.4 MB|387|
|2782|Instant Autodesk Revit 2013 Customization With .Net How-To|82|1.7 MB|19|
|2784|Instant Html5 2d Platformer|52|1.6 MB|106|
|2786|Instant Puppet 3 Starter Book|50|1.2 MB|31|
|2788|Introducing Html5 Game Development|120|5.0 MB|163|
|2790|Introduction To Mobile Telephone Systems 2nd Edition Book|92|1.6 MB|41|
|2792|Invent Your Own Computer Games With Python 3rd Edition Ebook|367|4.0 MB|212|
|2794|Io Programmo Magzine 111|99|8.6 MB|11|
|2796|Io Programmo Magzine 120|106|8.5 MB|10|
|2798|Io Programmo Magzine 87|117|9.2 MB|10|
|2800|Io Programmo Magzine 88|121|8.9 MB|17|
|2802|Io Programmo Magzine 89|119|8.9 MB|10|
|2804|Io Programmo Magzine 90|120|8.8 MB|12|
|2806|Io Programmo Magzine 92|118|8.3 MB|10|
|2808|Io Programmo Magzine 93|119|8.4 MB|10|
|2810|Io Programmo Magzine 94|119|8.7 MB|11|
|2812|Io Programmo Magzine 98|100|8.3 MB|11|
|2814|Io Programmo Magzine 99|96|8.8 MB|11|
|2816|iOS 7 Game Development|120|2.6 MB|47|
|2818|iOS 9 Game Development Essentials|329|6.1 MB|126|
|2820|iOS Game Development By Example|220|4.7 MB|125|
|2822|iOS Game Development Developing Games For Ipad Iphone And Ipod Touch|378|4.3 MB|122|
|2824|iOS Programming For Beginners|53|1.7 MB|33|
|2826|Iphone - Ipad Game Development For Dummies|508|5.1 MB|64|
|2828|iPhone Application Development For Dummies 4th Edition|465|15.6 MB|170|
|2830|IPv6 Address Planning|320|10.0 MB|83|
|2832|Ipv6 Deployment And Management Book|208|3.7 MB|58|
|2834|IPv6 Essentials 3rd Edition|412|8.5 MB|145|
|2836|Ipv6 Essentials, 2nd Edition Book|438|4.3 MB|45|
|2838|Ipv6 For Enterprise Networks|398|4.6 MB|125|
|2840|JavaScript For Dummies 4th Edition|387|43.9 MB|133|
|2842|Jenkins Essentials - Continuous Integration setting up the stage for a DevOps culture|186|8.4 MB|395|
|2844|Jmonkeyengine 3.0 Beginners Guide|352|5.5 MB|450|
|2846|Joomla 3 Seo And Performance Ebook|178|4.9 MB|227|
|2848|Jquery Game Development Essentials|244|2.7 MB|246|
|2850|Juniper Networks Warrior|429|6.4 MB|87|
|2852|Junos Enterprise Routing 2nd Edition Book|768|7.8 MB|40|
|2854|Landing Page Optimization|482|16.1 MB|20|
|2856|Learn Corona Sdk Game Development|277|5.8 MB|73|
|2858|Learn C++ For Game Development|296|2.4 MB|306|
|2860|Learning C - By Developing Games With Unity 3d|292|6.0 MB|243|
|2862|Learning Chef Automate your infrastructure using code and leverage DevOps with Chef|316|10.6 MB|61|
|2864|Learning Cocos2d-Js Game Development Ebook|188|2.9 MB|118|
|2866|Learning Construct 2 Ebook|234|4.2 MB|149|
|2868|Learning Dart Book|388|4.2 MB|77|
|2870|Learning Docker|240|2.7 MB|742|
|2872|Learning Force.Com Application Development|406|7.4 MB|21|
|2874|Learning Heroku Postgres Book|164|2.9 MB|27|
|2876|Learning Html5 Game Programming|254|4.8 MB|215|
|2878|Learning Java By Building Android Games|392|6.2 MB|149|
|2880|Learning Karaf Cellar Book|124|1.6 MB|38|
|2882|Learning MS Dynamics AX 2012 Programming|370|9.5 MB|119|
|2884|Learning Ngui For Unity|360|5.5 MB|146|
|2886|Learning Openstack Book|273|5.5 MB|175|
|2888|Learning Physics Modeling With Physx|104|2.2 MB|43|
|2890|Learning Search-Driven Application Development With Sharepoint 2013 Book|106|2.7 MB|64|
|2892|Learning Stencyl 3.X Game Development|336|6.1 MB|82|
|2894|Learning System Center App Controller|118|3.8 MB|46|
|2896|Learning Windows 8 Game Development|244|4.6 MB|66|
|2898|Letting Go Of The Words 2nd Edition Ebook|369|39.3 MB|431|
|2900|Libgdx Game Development By Example|280|3.9 MB|1011|
|2902|Liferay Portal 6.2 Enterprise Intranets|614|8.5 MB|134|
|2904|Linux Bible, 9th Edition|914|10.8 MB|444|
|2906|Linux- The Complete Manual|147|16.6 MB|196|
|2908|Livecode Mobile Development Beginners Guide Second Edition|256|6.0 MB|60|
|2910|Local Online Advertising For Dummies Ebook|394|4.6 MB|86|
|2912|Love For Lua Game Programming|106|1.7 MB|86|
|2914|LTE for UMTS - OFDMA and SC FDMA Based Radio Access|450|11.7 MB|81|
|2916|Lte Lte-Advanced And Wimax|305|3.6 MB|27|
|2918|Lte Security Book|292|3.3 MB|226|
|2920|Lte The Umts Long Term Evolution 2nd Edition Book|794|9.2 MB|43|
|2922|LTE The UMTS Long Term Evolution|626|8.3 MB|12|
|2924|Lua Game Development Cookbook|360|3.9 MB|256|
|2926|Lync Server Cookbook - Over 90 Recipes To Conigure Integrate And Manage Lync Server Deployment|392|10.5 MB|26|
|2928|Making Isometric Social Real-Time Games With Html5 Css3 And Javascript|154|2.5 MB|177|
|2930|Marketing Automation With Eloqua|136|4.1 MB|80|
|2932|Mastering Android Game Development|372|4.9 MB|376|
|2934|Mastering Autocad 2013 And Autocad LT 2013|1202|32.1 MB|45|
|2936|Mastering Citrix XenServer - Design and optimized virtualization solutions using Citrix XenServer 6.2|300|9.4 MB|48|
|2938|Mastering Gephi Network Visualization|378|11.0 MB|98|
|2940|Mastering Gradle|285|4.2 MB|118|
|2942|Mastering HR Management with SAP|666|21.6 MB|24|
|2944|Mastering Nmap Scripting Engine Book|332|1.7 MB|64|
|2946|Mastering Saltstack Book|306|2.6 MB|479|
|2948|Mastering Structured Data On The Semantic Web|244|7.9 MB|94|
|2950|Mastering Wireless Penetration Testing for Highly Secured Environments|220|10.7 MB|153|
|2952|Mathematical Game Theory And Applications|431|3.2 MB|159|
|2954|Mathematical Structures For Computer Graphics|411|2.7 MB|158|
|2956|Matlab Linear Algebra|264|6.9 MB|139|
|2958|MCSA 70 410 Cert Guide R2|1168|29.5 MB|217|
|2960|Microsoft Azure Essentials Book|246|7.1 MB|389|
|2962|Microsoft Biztalk Server 2010 Patterns|396|7.3 MB|36|
|2964|Microsoft Dynamics CRM 2011 Administration Bible|819|10.3 MB|82|
|2966|Microsoft Dynamics CRM 2011 Dashboards Cookbook|266|8.8 MB|64|
|2968|Microsoft Dynamics CRM 2011 Step by Step|448|12.7 MB|87|
|2970|Microsoft Dynamics CRM 4 Integration Unleashed|601|15.6 MB|62|
|2972|Microsoft Office Excel 2007 For Dummies|405|13.2 MB|47|
|2974|Microsoft System Center Configuration Manager Advanced Deployment|290|4.2 MB|94|
|2976|Microsoft System Center Powershell Essentials Book|140|1.9 MB|219|
|2978|Microsoft System Center Virtual Machine Manager 2012 Cookbook|342|9.6 MB|47|
|2980|Microsoft Xna 4.0 Game Development Cookbook|357|2.6 MB|111|
|2982|Microsoft Xna Unleashed|541|5.3 MB|17|
|2984|Migrating Applications To Ipv6 Book|50|1.1 MB|16|
|2986|Mimo Wireless Communications|343|4.0 MB|98|
|2988|Mimo-Ofdm For Lte Wifi And Wimax|694|8.9 MB|19|
|2990|Mimo-Ofdm Wireless Communications With Matlab|457|5.3 MB|323|
|2992|Minecraft Construction For Dummies Portable Edition Ebook|226|3.5 MB|57|
|2994|Minecraft Modding With Forge|278|6.6 MB|104|
|2996|Mining the Social Web 2nd Edition|448|8.9 MB|48|
|2998|Mining The Social Web|356|5.6 MB|32|
|3000|Mobile Application Security|432|4.4 MB|41|
|3002|Mobile Handset Design Book|589|4.1 MB|43|
|3004|Mobile Intelligence Book|721|7.4 MB|45|
|3006|Mobile Opportunistic Networks|286|4.4 MB|93|
|3008|Mobile Peer To Peer - P2P|274|2.7 MB|33|
|3010|Mobile Positioning And Tracking Book|300|3.6 MB|46|
|3012|Mobile WiMAX Understanding IEEE 802.16m Radio Access Technology - Networking Book|767|10.4 MB|75|
|3014|Monopoly TYCOON Primas Official Strategy Guide|153|10.2 MB|26|
|3016|MPLS-Enabled Applications - Networking Book|435|8.3 MB|89|
|3018|Multi-Carrier And Spread Spectrum Systems Book|380|3.6 MB|19|
|3020|Multimedia Messaging Service Book|270|1.5 MB|38|
|3022|Multiplayer Game Development With Html5|180|2.5 MB|363|
|3024|Netcat Starter Book|65|3.1 MB|51|
|3026|Network Graph Analysis And Visualization With Gephi Book|116|3.4 MB|79|
|3028|Network Modeling And Simulation Book|300|2.5 MB|92|
|3030|Network Security Auditing|517|11.4 MB|112|
|3032|Network Troubleshooting Tools Book|269|2.4 MB|66|
|3034|Networking All in One For Dummies 4th Edition - Networking Book|916|10.1 MB|66|
|3036|Networking All in One For Dummies 4th Edition|916|12.3 MB|125|
|3038|Networking For Dummies 10th Edition|459|10.5 MB|289|
|3040|Neural Networks And Computing|322|4.6 MB|107|
|3042|Next Generation Mobile Systems 3g Beyond|406|5.0 MB|30|
|3044|Nginx Essentials Book|151|2.3 MB|154|
|3046|Nginx HTTP Server 3rd Edition Book|443|3.4 MB|357|
|3048|Nmap 6 Network Exploration And Security Auditing Cookbook|318|2.8 MB|291|
|3050|Node.Js High Performance|136|2.7 MB|248|
|3052|Noname Clevo 888e Sager Np888x Service Manual|197|10.9 MB|7|
|3054|Noname Clevo D500e D510e D520e D530e Sager Np5690 Service Manual|134|10.7 MB|9|
|3056|Noname Mitac 8399 Service Manual|174|3.3 MB|8|
|3058|Nosql For Mere Mortals|630|11.0 MB|210|
|3060|Office 2013 for Dummies|435|15.0 MB|20|
|3064|Official ISC2 Guide to the CSSLP CBK Second Edition|781|12.6 MB|47|
|3066|Online Privacy Thinking Critically Reference Point|80|3.1 MB|11|
|3068|Opencart Theme And Module Development Ebook|208|3.3 MB|928|
|3070|OpenCV 3 Blueprints|514|10.5 MB|899|
|3072|Openframeworks Essentials|206|4.0 MB|57|
|3074|Opengl Game Development|497|4.2 MB|122|
|3076|Openstack Cloud Application Development Book|228|3.5 MB|80|
|3078|Openstack Essentials Book|182|3.5 MB|72|
|3080|Openvpn Building And Integrating Virtual Private Networks|270|6.7 MB|212|
|3082|Oracle Application Express 4 Recipes|352|20.3 MB|26|
|3084|Oracle Solaris 11 Advanced Administration Cookbook|478|4.2 MB|108|
|3086|Outlook 2007 For Dummies|382|12.9 MB|31|
|3088|Outlook 2013 For Dummies|387|11.0 MB|77|
|3090|Ouya Game Development By Example|268|5.2 MB|46|
|3092|Packet Guide To Core Network Protocols Book|160|3.1 MB|235|
|3094|Packet Tracer Network Simulator Book|134|2.5 MB|204|
|3096|Panda3d 1.6 Game Engine|356|6.4 MB|49|
|3098|Pattern Oriented Software Architecture For Dummies|386|9.7 MB|114|
|3100|Pattern-Oriented Software Architecture For Dummies|386|9.7 MB|52|
|3102|Penetration Testing - A Hands On Introduction To Hacking|531|10.4 MB|684|
|3104|Photoshop CC The Missing Manual|928|31.6 MB|108|
|3106|Photoshop CS3 Restoration And Retouching Bible|514|24.6 MB|65|
|3108|Photoshop CS4 All In One For Dummies|722|31.0 MB|45|
|3110|Photoshop CS5 The Missing Manual|816|19.6 MB|63|
|3112|Photoshop CS6 The Missing Manual|886|41.4 MB|195|
|3114|Photoshop CS6 Unlocked 2nd Edition Book|442|24.1 MB|265|
|3116|Photoshop Elements 13 For Dummies|452|18.9 MB|197|
|3118|PHP MySQL JavaScript HTML5 All in One For Dummies|724|9.6 MB|536|
|3120|Physics For Game Programmers|457|5.2 MB|107|
|3123|2D Graphics Programming for Games|240|4.9 MB|361|
|3125|3D Game Development with Microsoft Silverlight 3|452|9.9 MB|56|
|3127|3D Video Coding for Embedded Devices|219|4.6 MB|18|
|3129|98-374 Gaming Development Fundamentals|238|8.7 MB|93|
|3131|A Game Design Vocabulary|236|6.1 MB|113|
|3135|Abusing the Internet of Things Blackouts, Freakouts and Stakeouts|291|7.9 MB|147|
|3137|Adobe Creative Cloud Design Tools All in One For Dummies|1059|32.6 MB|62|
|3141|Advanced Wireless Communications 4G Cognitive and Cooperative Broadband Technology 2nd Edition|890|17.4 MB|67|
|3143|An Architectural Approach to Level Design|456|11.7 MB|298|
|3146|Android Game Programming For Dummies|387|9.4 MB|229|
|3149|Android Programming The Big Nerd RANCH Guide|625|13.3 MB|425|
|3151|Apple Watch And Iphone Fitness Tips And Tricks|445|14.0 MB|31|
|3153|Applied Architecture Patterns on the Microsoft Platform 2nd Edition|456|5.7 MB|26|
|3155|Arduino by Example - Design And Build Fantastic Projects And Devices Using The Arduino Platform|242|7.6 MB|516|
|3157|Arduino Development Cookbook|246|3.8 MB|685|
|3159|Arduino Home Automation Projects|132|3.9 MB|1012|
|3161|Arduino Wearables|330|7.8 MB|303|
|3163|ARM Assembly Language Fundamentals and Techniques, Second Edition|448|3.4 MB|36|
|3165|ARM Assembly Language with Hardware Experiments|144|5.5 MB|54|
|3167|Banana Pi Cookbook|200|4.5 MB|95|
|3169|BeagleBone Black Cookbook|616|7.2 MB|103|
|3171|BeagleBone Cookbook|655|15.5 MB|106|
|3173|BeagleBone Essentials|240|2.9 MB|35|
|3175|BeagleBone For Dummies|436|13.6 MB|122|
|3177|Beginning 3D Game Development with Unity 4, 2nd Edition|796|27.2 MB|125|
|3179|Beginning Android Games, 2nd Edition|706|8.2 MB|179|
|3181|Beginning Android Games|679|15.3 MB|111|
|3183|Beginning Facebook Game Apps Development|423|12.0 MB|205|
|3187|Beginning iOS Game Development|435|6.8 MB|58|
|3189|Beginning iOS Social Games|301|4.4 MB|36|
|3191|Beginning Java 8 Games Development|475|33.4 MB|358|
|3193|Beginning Kinect Programming with the Microsoft Kinect SDK|321|3.0 MB|139|
|3195|Beginning RPG Maker VX Ace|317|11.2 MB|25|
|3197|Blender for Animation and Film-Based Production|279|7.2 MB|19|
|3199|Build an Awesome PC, 2014 Edition|110|4.2 MB|14|
|3201|Build an HTPC - The Geek|26|3.0 MB|13|
|3203|Build your own 2D Game Engine and Create Great Web Games|481|5.3 MB|335|
|3205|Building a Game with Unity and Blender|250|5.9 MB|671|
|3207|Building A Home Security System With Arduino|230|2.5 MB|767|
|3209|Building Levels in Unity|274|6.6 MB|296|
|3211|Buying a Computer For Dummies, 2005 Edition|339|3.3 MB|15|
|3213|Canon EOS 7D Mark II For Dummies|323|14.8 MB|90|
|3215|Channel Coding Techniques for Wireless Communications|407|18.2 MB|204|
|3217|Cinder Creative Coding Cookbook|352|3.3 MB|41|
|3219|Cisco ASA, 2nd Edition|1151|28.1 MB|19|
|3221|Cisco Networking Essentials|450|63.1 MB|692|
|3223|Cisco Unity Connection|623|28.1 MB|37|
|3225|Cloud Database Development and Management|479|10.5 MB|46|
|3227|Cocos2d-x Game Development Blueprints|392|4.1 MB|225|
|3229|Cognitive Radio Technology|649|6.0 MB|18|
|3231|CompTIA A pus 220-801 and 220-802 Cert Guide 3rd Edition|174|1.2 MB|40|
|3233|Computer Architecture|364|3.0 MB|18|
|3235|Computer Organization and Architecture, 9th Edition|787|4.0 MB|27|
|3237|Computer System Design System on Chip|350|4.2 MB|21|
|3239|Construct 2 Game Development by Example|230|5.4 MB|510|
|3241|Corona SDK Mobile Game Development Beginners Guide, 2nd Edition|372|5.5 MB|254|
|3243|Create Mobile Games with Corona|258|4.1 MB|41|
|3245|Creating E-Learning Games with Unity|246|3.0 MB|206|
|3247|CryENGINE 3 Game Development|354|10.8 MB|81|
|3249|Cryptographic Hardware and Embedded Systems CHES 2015|705|23.8 MB|229|
|3251|Cyber Operations - Building Defending and Attacking Modern Computer Networks|762|17.2 MB|331|
|3253|Designing the User Experience of Game Development Tools|164|2.8 MB|155|
|3257|Embedded Systems Design with FPGAs|279|5.4 MB|23|
|3259|Enhanced For Loop Java Program|3|653.4 KB|39|
|3261|Enterprise Games - Using Game Mechanics to Build a Better Business|215|5.2 MB|70|
|3263|Essential Facebook Development|481|6.7 MB|147|
|3265|Express.Js Deep Api Reference|152|4.8 MB|124|
|3267|Fbml Essentials|190|2.2 MB|13|
|3269|Fix Your Own Computer For Seniors For Dummies|386|11.2 MB|40|
|3273|Flash With Drupal|380|7.9 MB|40|
|3275|Foundation Drupal 7|337|12.4 MB|107|
|3277|Foundations of BizTalk Server 2006|263|6.6 MB|16|
|3279|Foundations Of Programming|79|1.2 MB|16|
|3281|FPGA Design - Best Practices for Team-based Reuse|260|5.8 MB|54|
|3283|Friend Functions And Friend Classes - C++ Lecture 9|12|596.4 KB|42|
|3287|Functional Programming In Java|182|2.7 MB|88|
|3289|Fundamental 2D Game Programming with Java|654|18.4 MB|845|
|3291|Fundamentals of Digital Logic with VHDL Design 3rd edition|961|8.8 MB|167|
|3293|Fundamentals Of Python Programming|429|6.8 MB|152|
|3295|Game AI Pro 2 Collected Wisdom of Game AI Professionals|566|7.1 MB|698|
|3297|Game Analytics Maximizing the Value|791|11.1 MB|138|
|3299|Game Coding Complete Fourth Edition|959|5.0 MB|207|
|3301|Game Design Essentials|322|12.8 MB|248|
|3303|Game Design Workshop 3rd Edition|528|8.9 MB|1062|
|3305|Game Development Tool Essentials|201|5.0 MB|179|
|3307|Game Development with Unity 2nd Edition|465|6.2 MB|158|
|3309|Game Engine Architecture|853|7.6 MB|152|
|3311|GameMaker Game Programming with GML|351|4.2 MB|131|
|3313|GameMaker Studio For Dummies|356|7.2 MB|57|
|3315|Gamestar Mechanic For Dummies|355|18.3 MB|74|
|3317|Gamification by Design|210|5.1 MB|165|
|3319|Get Fit with Apple Watch|212|4.9 MB|13|
|3321|Getting Started with Clickteam Fusion|114|3.3 MB|47|
|3323|Getting Started with Cubieboard|162|3.6 MB|31|
|3325|Getting Started With Grunt The Javascript Task Runner|132|1.4 MB|79|
|3327|Getting Started With Magento Extension Development|128|1.5 MB|192|
|3330|Getting Started With Oauth 2.0|79|6.2 MB|263|
|3334|Google Nexus 6 User Manual|148|797.9 KB|34|
|3336|Guide to Cisco Routers Configuration - Becoming a Router Geek|84|459.6 KB|93|
|3338|Guide to Computer Network Security, 3rd edition|550|7.0 MB|228|
|3340|Hacking Raspberry Pi|523|19.1 MB|1185|
|3342|Hacking the Kinect|261|5.6 MB|441|
|3346|Healthy SQL|395|11.7 MB|53|
|3348|High Level Synthesis - from Algorithm to Digital Circuit|307|6.1 MB|27|
|3350|High Performance Drupal|263|6.5 MB|66|
|3352|History of Wireless|681|26.7 MB|22|
|3356|How To Become A Programmer|33|1.0 MB|31|
|3358|How To Create The Next Facebook|199|1.1 MB|137|
|3360|How To Get Input From User In Java Program|4|661.9 KB|44|
|3362|How To Upload A Catalog On Magento|37|2.6 MB|92|
|3366|HTML5 Games Development by Example|352|6.4 MB|142|
|3368|Hypertext Preprocessor Php Basics - Php Lecture  6|43|839.1 KB|33|
|3370|Information Architecture Fourth Edition|485|11.7 MB|249|
|3372|Instant PLC Programming with RSLogix 5000|68|1.0 MB|109|
|3374|Intel Xeon Phi Coprocessor Architecture and Tools|220|2.7 MB|16|
|3376|Interactive Computer Graphics, 6th Edition|778|9.5 MB|85|
|3378|Interface In Java Program|3|648.4 KB|42|
|3380|Introducing Microsoft Sql Server 2012|287|7.5 MB|91|
|3382|Introduction Object Oriented Programming Using C++ - C++ Lecture 1|12|1.1 MB|55|
|3384|Introduction To Asp.Net - Asp.Net Lecture 1|15|807.0 KB|57|
|3386|Introduction To Asp.Net - Asp.Net Lecture 2|25|773.3 KB|60|
|3388|Introduction to Computer Networks and Cybersecurity|1373|39.5 MB|1401|
|3390|Introduction To Java - Java Lecture 1|40|1.1 MB|36|
|3392|Introduction To Web - Php Lecture 1|43|1.2 MB|33|
|3394|Introduction To Web Services - Asp.Net Lecture 10|10|1.2 MB|88|
|3396|Invent Your Own Computer Games With Python 2nd Edition|473|5.8 MB|72|
|3398|Ios 6 Programming Cookbook|976|14.4 MB|24|
|3400|Ios 8 Swift Programming Cookbook|901|10.8 MB|32|
|3402|Ios Components And Frameworks|573|7.7 MB|42|
|3404|iOS Game Programming Cookbook|505|7.6 MB|97|
|3406|Ios Uicollectionview 2nd Edition|192|3.4 MB|41|
|3408|iPad mini For Dummies|387|19.0 MB|35|
|3410|iPhone Games Projects|282|5.0 MB|58|
|3412|Java 7 Concurrency Cookbook|364|3.0 MB|102|
|3414|Java 7 Instant Help For Java Programmers 2nd Edition Book|215|6.0 MB|62|
|3416|Java Abstract Classes Interfaces - Java Lecture 8|19|690.4 KB|43|
|3418|Java Annimation - Java Lecture 5|6|581.9 KB|34|
|3420|Java Applet Basics|10|978.2 KB|29|
|3422|Java Classes And Objects - Java Lecture 4|34|1,010.6 KB|38|
|3424|Java Collection Framework - Java Lecture 21|26|868.5 KB|34|
|3426|Java Collection Framework - Java Lecture 23|22|663.2 KB|38|
|3428|Java Collections Framework - Java Lecture 22|21|758.5 KB|35|
|3430|Java Collections Framework|5|953.6 KB|33|
|3432|Java Constructor Tutorial With Code Examples|7|706.4 KB|38|
|3434|Java Data Structures|3|933.6 KB|41|
|3436|Java Documentation Comments|5|951.7 KB|30|
|3438|Java Ee 7 Essentials|362|12.1 MB|294|
|3440|Java Ee 7 Recipes|736|9.2 MB|194|
|3442|Java Events Handling - Java Lecture 13|21|772.4 KB|28|
|3444|Java Exception Handling Tutorial With Example Programs|8|676.4 KB|45|
|3446|Java Exceptions - Java Lecture 9|20|697.5 KB|37|
|3448|Java For Loop Program|5|679.1 KB|30|
|3450|Java Generics|4|942.9 KB|34|
|3452|Java Graphics Class - Java Lecture 15|25|745.9 KB|53|
|3454|Java Gui - Java Lecture 11|39|895.5 KB|38|
|3456|Java Gui - Java Lecture 12|40|911.5 KB|38|
|3458|Java Hello World Program|3|630.5 KB|33|
|3460|Java If Else Program|5|691.3 KB|31|
|3462|Java Multithreading|9|998.0 KB|52|
|3464|Java Networking - Java Lecture 26|17|1.0 MB|69|
|3466|Java Networking|8|966.5 KB|59|
|3468|Java Passing Objects In Network Programs - Java Lecture 28|11|570.5 KB|32|
|3470|Java Persistence With Mybatis 3|132|1.5 MB|93|
|3472|Java Program For Binary Search|4|658.5 KB|41|
|3474|Java Program For Linear Search|4|660.4 KB|38|
|3476|Java Program Print Prime Numbers|5|653.3 KB|37|
|3478|Java Program To Add Two Matrices|4|664.1 KB|35|
|3480|Java Program To Add Two Numbers|4|649.2 KB|36|
|3482|Java Program To Bubble Sort|4|659.4 KB|42|
|3484|Java Program To Check Armstrong Number|4|667.6 KB|36|
|3486|Java Program To Check Palindrome|4|657.0 KB|36|
|3488|Java Program To Compare Two Strings|3|651.6 KB|40|
|3490|Java Program To Convert Fahrenheit To Celsius Program|3|643.0 KB|35|
|3492|Java Program To Display Date And Time Print Date And Time Using Java Program|3|644.9 KB|43|
|3494|Java Program To Find All Substrings Of A String|3|646.3 KB|36|
|3496|Java Program To Find Factorial|5|653.3 KB|35|
|3498|Java Program To Find Largest Of Three Numbers|3|642.5 KB|37|
|3500|Java Program To Find Odd Or Even|4|652.1 KB|35|
|3502|Java Program To Generate Random Numbers|3|650.5 KB|40|
|3504|Java Program To Get Ip Address|3|634.6 KB|45|
|3506|Java Program To Multiply Two Matrices|4|660.1 KB|37|
|3508|Java Program To Open Notepad|3|628.0 KB|48|
|3510|Java Program To Perform Garbage Collection|3|645.7 KB|45|
|3512|Java Program To Print Alphabets|4|637.6 KB|35|
|3514|Java Program To Print Floyd&#8217;s Triangle|3|644.4 KB|38|
|3516|Java Program To Print Multiplication Table|4|658.7 KB|39|
|3518|Java Program To Reverse A String|3|643.1 KB|40|
|3520|Java Program To Reverse Number|3|643.9 KB|39|
|3522|Java Program To Swap Two Numbers|4|646.4 KB|38|
|3524|Java Program To Transpose Matrix|3|646.1 KB|40|
|3526|Java Programming Applets And Drawing - Java Lecture 16|20|755.7 KB|45|
|3528|Java Programming Event Handling - Java Lecture 14|17|577.1 KB|45|
|3530|Java Programming Io Streams - Java Lecture 25|24|720.7 KB|49|
|3532|Java Programming Strings - Java Lecture 10|20|694.3 KB|41|
|3534|Java Programs|12|746.5 KB|46|
|3536|Java Sending Email|5|952.3 KB|53|
|3538|Java Serialization|3|938.1 KB|45|
|3540|Java Static Block Program|4|662.5 KB|41|
|3542|Java Static Method Program|5|674.9 KB|47|
|3544|Java Syntax And String Methods Program|7|697.0 KB|46|
|3546|Java Threads - Java Lecture 16|23|678.0 KB|51|
|3548|Java Threads - Java Lecture 17|18|731.5 KB|52|
|3550|Java Threads Deadlock - Java Lecture 20|14|1.2 MB|54|
|3552|Java Threads Synchronization - Java Lecture 18|33|651.7 KB|55|
|3554|Java Udp - Java Lecture 27|16|600.4 KB|40|
|3556|Java While Loop Program|7|679.8 KB|44|
|3558|Java- Classes And Packages - Java Lecture 6|26|656.7 KB|54|
|3560|Javafx 8 2nd Edition Book|409|9.3 MB|77|
|3562|Javamail Api|97|4.7 MB|107|
|3564|Javascript - Php Lecture 7|58|1.3 MB|53|
|3566|Javascript Cookbook 2nd Edition Book|633|8.2 MB|185|
|3568|Javascript Programmers Reference|289|3.0 MB|156|
|3570|Javascript Step By Step 3rd Edition Book|481|7.8 MB|197|
|3572|Javascript Unit Testing|190|2.3 MB|96|
|3574|Jdbc Java Database Connectivity - Java Lecture 29|26|1,002.6 KB|77|
|3576|Juniper MX Series|902|11.4 MB|104|
|3578|Kinect for Windows SDK Programming Guide|392|6.7 MB|30|
|3580|Kinect Hacks|279|8.0 MB|415|
|3582|Kinect in Motion - Audio and Visual Tracking by Example|112|2.1 MB|20|
|3584|Learn 2D Game Development with C-sharp|285|5.0 MB|158|
|3586|Learn Lua for iOS Game Development|410|6.5 MB|44|
|3588|Learn Raspberry Pi Programming with Python|244|3.6 MB|625|
|3590|Learn Sprite Kit for iOS Game Development|243|4.4 MB|99|
|3592|Learn SpriteBuilder for iOS Game Development|440|9.2 MB|63|
|3594|Learn Unity 4 for iOS Game Development|543|18.3 MB|111|
|3596|Learn Unity for 2D Game Development|306|9.9 MB|276|
|3598|Learn Unity3D Programming with UnityScript|411|13.9 MB|220|
|3600|Learning AndEngine|286|3.9 MB|52|
|3602|Learning Android Game Programming|476|6.0 MB|219|
|3604|Learning Ansible - Use Ansible to Configure Systems Deploy Software and Orchestrate Advanced IT Tasks|309|9.3 MB|367|
|3606|Learning Banana Pi|178|4.0 MB|52|
|3608|Learning BeagleBone Python Programming|196|4.3 MB|269|
|3612|Learning Cocos2D|634|9.8 MB|10|
|3614|Learning C++ by Creating Games with UE4|342|9.4 MB|126|
|3616|Learning Game AI Programming with Lua|680|5.3 MB|323|
|3618|Learning iOS 8 Game Development Using Swift|366|8.4 MB|79|
|3620|Learning iPhone Game Development with Cocos2d 3.0|434|8.3 MB|49|
|3622|Learning LibGDX Game Development, 2nd Edition|478|8.0 MB|88|
|3624|Learning NServiceBus|136|1.3 MB|12|
|3626|Learning Objective-C by Developing iPhone Games|284|6.6 MB|64|
|3628|Learning OpenShift|304|9.8 MB|132|
|3630|Learning Puppet for Windows Server|234|13.0 MB|113|
|3632|Learning Python with Raspberry Pi|288|2.1 MB|875|
|3634|Learning Raspberry Pi|259|4.7 MB|589|
|3636|Learning ROS for Robotics Programming - Second Edition|458|9.1 MB|359|
|3638|Learning RSLogix 5000 Programming|224|3.8 MB|63|
|3640|Learning Unity 2D Game Development by Example|491|5.9 MB|1615|
|3642|Learning Unity Android Game Development|338|21.7 MB|1064|
|3644|Learning Unreal Engine Android Game Development|300|12.1 MB|324|
|3646|Learning Unreal Engine iOS Game Development|354|8.4 MB|127|
|3648|Learning XNA 4.0|540|7.2 MB|36|
|3650|Libgdx Cross platform Game Development Cookbook|913|7.8 MB|1257|
|3652|LibGDX Game Development Essentials|216|5.0 MB|210|
|3654|Make a 2D RPG in a Weekend|236|4.9 MB|37|
|3656|Making Embedded Systems|314|2.8 MB|203|
|3658|Making Things Talk, Second Edition|496|29.9 MB|50|
|3660|Mastering BeagleBone Robotics|234|10.6 MB|79|
|3662|Mastering Cocos2d Game Development|436|5.5 MB|90|
|3664|Mastering Leap Motion|361|6.2 MB|64|
|3666|Mastering ServiceNow|606|11.0 MB|1060|
|3668|Mastering the Raspberry Pi|482|5.2 MB|627|
|3670|Mastering UDK Game Development|290|11.5 MB|88|
|3672|Mastering Unity Scripting|380|9.0 MB|361|
|3674|Mastering VMware Horizon 6|640|28.9 MB|87|
|3676|Memory Allocation Problems in Embedded Systems Optimization Method|189|1.6 MB|25|
|3678|Micro Nanosystems and Systems on Chips|318|8.2 MB|21|
|3680|Microsoft XNA Game Studio 4.0 Learn Programming Now!|465|4.7 MB|84|
|3682|Mobile - Social Game Design- Monetization Methods and Mechanics 2nd Edition|226|7.2 MB|232|
|3684|Mobile Communication Systems|466|30.7 MB|49|
|3686|Mobile Radio Networks, 2nd Edition|1177|63.3 MB|28|
|3688|Mobility Data - Modeling, Management and Understanding|393|11.3 MB|10|
|3690|MPLS in the SDN Era|919|14.3 MB|521|
|3692|Mule ESB Cookbook|428|13.7 MB|239|
|3694|Multi-Threaded Game Engine Design|593|4.6 MB|119|
|3696|Network Analysis Using Wireshark Cookbook|452|13.0 MB|448|
|3698|Network Security A Beginners Guide Third Edition|337|14.2 MB|954|
|3700|Optimizing HPC Applications with Intel Cluster Tools|291|4.5 MB|16|
|3702|Penetration Testing with Raspberry Pi|208|7.4 MB|512|
|3704|pfSense 2 Cookbook|240|22.6 MB|112|
|3706|Photoshop CS5 All In One For Dummies|778|22.4 MB|136|
|3708|Physics for Game Developers 2nd Edition|577|5.6 MB|250|
|3710|Physics for JavaScript Games Animation and Simulations|490|5.1 MB|120|
|3712|PlayStation Mobile Development Cookbook|322|5.5 MB|21|
|3716|Practical Intrusion Analysis|480|8.6 MB|34|
|3718|Practical Malware Analysis|802|9.2 MB|50|
|3720|Practical Salesforce.com Development Without Code|306|9.8 MB|236|
|3722|Practical SharePoint 2010 Information Architecture|259|10.0 MB|54|
|3724|Practical Web Analytics For User Experience|251|21.2 MB|141|
|3726|Principles of Communications 7th Edition|746|9.9 MB|207|
|3728|Pro Android Flash|463|16.4 MB|97|
|3730|Pro Android Games 3rd Edition|395|6.2 MB|265|
|3732|Pro Android Graphics - Android Digital Imaging Formats Concepts and Optimization|605|42.5 MB|354|
|3734|Pro Android Web Game Apps|657|8.1 MB|304|
|3736|Pro CSS and HTML Design Patterns|527|7.9 MB|105|
|3738|Pro Dns And Bind 10|679|5.1 MB|139|
|3740|Pro Git, 2nd Edition - Networking Book|441|8.9 MB|262|
|3742|Pro HTML5 Games|357|5.2 MB|156|
|3744|Pro SharePoint 2010 Development for Office 365|257|8.6 MB|44|
|3746|Pro SharePoint 2010 Governance|326|9.5 MB|36|
|3748|Pro SharePoint 2013 Business Intelligence Solutions|432|22.5 MB|88|
|3750|Pro SQL Server Administration|1008|32.8 MB|113|
|3752|Pro Unity Game Development with C-|335|10.1 MB|115|
|3754|Pro WCF 4 Practical Microsoft SOA Implementation 2nd Edition|452|16.9 MB|48|
|3756|Pro Web Gadgets for Mobile and Desktop|373|9.2 MB|67|
|3758|Product Development Process for Open Source Hardware|94|781.4 KB|25|
|3760|Professional Android Open Accessory Programming with Arduino|412|12.1 MB|426|
|3762|Professional Flash Lite Mobile Development|568|31.8 MB|46|
|3764|Professional Flash Mobile Development|338|10.4 MB|57|
|3766|Professional HTML5 Mobile Game Development|554|5.1 MB|177|
|3768|Professional SharePoint 2010 Field Guide|458|12.7 MB|44|
|3770|Professional Team Foundation Server 2013|914|21.8 MB|26|
|3772|Programming Google Glass, 2nd Edition|299|4.5 MB|41|
|3774|Programming Language Processors in Java Compilers and Interpreters|438|27.2 MB|52|
|3776|Programming the Raspberry Pi|134|7.1 MB|619|
|3778|Programming With The Kinect For Windows Software Development Kit|224|2.7 MB|70|
|3780|Pulling Strings With Puppet Book|194|2.7 MB|62|
|3782|Puppet 2.7 Cookbook Book|171|1.8 MB|32|
|3784|Puppet Reporting And Monitoring Book|186|2.9 MB|73|
|3786|Python Hacking Essentials|266|9.8 MB|1283|
|3788|Python Penetration Testing Essentials Book|178|3.5 MB|190|
|3790|Radar Systems Analysis And Design Using Matlab Second Edition|533|4.6 MB|101|
|3792|Radio Interface System Planning For Gsmgprsumts|294|6.8 MB|15|
|3794|Radio Network Planning and Optimisation for UMTS 2nd Edition|664|13.0 MB|130|
|3796|Raspberry Pi 2|39|609.6 KB|528|
|3798|Raspberry Pi 2nd Edition|169|4.2 MB|265|
|3800|Raspberry Pi A Quick Start Guide|120|2.5 MB|132|
|3802|Raspberry Pi Android Projects|219|2.9 MB|1151|
|3804|Raspberry Pi Computer Vision Programming|178|4.6 MB|667|
|3806|Raspberry Pi Cookbook for Python Programmers|402|7.2 MB|825|
|3808|Raspberry Pi Cookbook|410|12.4 MB|575|
|3810|Raspberry Pi Embedded Projects Hotshot|250|5.5 MB|520|
|3812|Raspberry Pi for Beginners 2nd Edition|180|28.2 MB|242|
|3814|Raspberry Pi For Dummies|435|8.8 MB|776|
|3816|Raspberry Pi for Secret Agents|153|2.6 MB|445|
|3818|Raspberry Pi Gaming 2nd Edition|140|4.4 MB|226|
|3820|Raspberry Pi Hardware Reference|234|2.2 MB|641|
|3822|Raspberry Pi Home Automation with Arduino Second Edition|148|2.1 MB|659|
|3824|Raspberry Pi LED Blueprints|181|5.0 MB|564|
|3826|Raspberry Pi Networking Cookbook|204|4.8 MB|710|
|3828|Raspberry Pi Projects for Kids|96|2.1 MB|661|
|3830|Raspberry Pi Server Essentials Book|116|2.2 MB|320|
|3832|Raspberry Pi Server Essentials|116|1.7 MB|605|
|3834|Raspberry Pi Super Cluster|126|1.2 MB|613|
|3836|Raspberry Pi System Software Reference|124|1.3 MB|729|
|3838|Real-Time Visual Effects for Game Programming|238|12.3 MB|89|
|3840|Releasing HTML5 Games for Windows 8|159|4.1 MB|99|
|3842|Resilient Computer System Design|271|6.2 MB|32|
|3844|Reverse Engineering for Beginners|942|8.5 MB|25|
|3846|RFID Handbook, 3rd Edition|480|4.5 MB|30|
|3848|Roaming In Wireless Networks Book|338|2.4 MB|140|
|3850|Robot Building for Beginners, Third Edition|472|16.1 MB|211|
|3852|Roxio Easy Media Creator 8 For Dummies|386|6.9 MB|16|
|3854|Salesforce CRM Admin Cookbook - Over 40 recipes to make effective use of Salesforce CRM|266|11.2 MB|51|
|3856|Salt Cookbook|350|2.1 MB|40|
|3858|Salt Essentials Book|178|2.3 MB|61|
|3860|Sams Teach Yourself Google Adwords In 10 Minutes|235|5.8 MB|210|
|3862|Sams Teach Yourself Google Analytics In 10 Minutes|241|6.0 MB|220|
|3864|Sams Teach Yourself Microsoft Dynamics Crm 2011 in 24 Hours|518|19.2 MB|117|
|3866|Sams Teach Yourself Windows Phone 7 Game Programming In 24 Hours|384|6.6 MB|61|
|3868|Samsung Galaxy S6 for Dummies|412|9.6 MB|48|
|3870|SAP BusinessObjects Dashboards 4.0 Cookbook|352|14.7 MB|39|
|3872|SAP BusinessObjects Reporting Cookbook|380|9.8 MB|109|
|3874|SAP GRC For Dummies|362|21.5 MB|72|
|3876|Sap Hcm - A Complete Tutorial|380|8.3 MB|96|
|3878|Science Fiction Video Games|528|6.3 MB|145|
|3880|Scientific Computing With Matlab And Octave 2nd Edition|342|6.7 MB|116|
|3882|Scratch 2.0 Beginners Guide 2nd Edition|296|5.5 MB|165|
|3884|Scratch 2.0 Game Development|330|6.3 MB|99|
|3886|Scratch Cookbook|262|7.8 MB|45|
|3888|Scratch For Kids For Dummies|418|15.7 MB|198|
|3890|Sdl Game Development Ebook|256|2.6 MB|243|
|3892|Secure Development for Mobile Apps|460|3.0 MB|28|
|3894|Secure Wireless Sensor Networks|180|3.1 MB|72|
|3896|Securing Cloud Services|329|5.8 MB|26|
|3898|Security And Privacy For Mobile Healthcare Networks Book|130|2.8 MB|24|
|3900|Security In Wireless Sensor Networks Book|97|1.3 MB|77|
|3902|Security Intelligence - A Practitioners Guide to Solving Enterprise Security Challenges|363|10.3 MB|887|
|3904|Server Load Balancing Book|182|3.6 MB|23|
|3906|SFML Blueprints|298|3.1 MB|613|
|3908|Sfml Essentials Ebook|156|2.8 MB|200|
|3910|Sfml Game Development Ebook|296|3.0 MB|551|
|3912|SharePoint 2010 Development with Silverlight|610|16.4 MB|29|
|3914|Sharepoint 2010 For Dummies|412|9.1 MB|42|
|3916|SharePoint 2010 for Project Management, 2nd Edition|228|9.6 MB|61|
|3918|SharePoint 2010 How To|393|15.7 MB|75|
|3920|Short Message Service - SMS|195|2.0 MB|20|
|3922|SIM City 3000 Primas Official Strategy Guide|545|13.2 MB|29|
|3924|Smart Card Handbook, 4th Edition|1072|12.4 MB|21|
|3926|Smashing CSS|305|20.0 MB|202|
|3928|SolarWinds Orion Network Performance Monitor|336|9.7 MB|57|
|3930|Solving Odes With Matlab|273|1.8 MB|75|
|3932|Sparrow iOS Game Framework, Beginners Guide|274|3.7 MB|45|
|3934|Splunk Developers Guide Book|180|2.9 MB|179|
|3936|Starting an Online Business For Dummies 6th Edition|436|7.3 MB|24|
|3938|Statistical Analysis with Excel For Dummies 3rd Edition|530|37.8 MB|132|
|3940|Stencyl Essentials|289|8.4 MB|129|
|3942|Stochastic Modeling And Analysis Of Telecoms Networks Book|384|2.5 MB|37|
|3944|Storm Real Time Processing Cookbook|254|2.6 MB|15|
|3946|Sudoku Programming With C|285|4.5 MB|211|
|3948|Super Scratch Programming Adventure|162|53.0 MB|17|
|3950|Supporting Windows 8, 2nd Edition|160|43.6 MB|22|
|3952|System Center 2012 R2 Virtual Machine Manager Cookbook - Second Edition|428|12.6 MB|158|
|3954|Systems Architecture, 6 edition|658|11.0 MB|30|
|3956|Systems Engineering In Wireless Communications|357|5.7 MB|109|
|3958|Tableau Data Visualization Cookbook|172|4.0 MB|173|
|3960|TCPIP Illustrated Volume-1 2nd Edition|1059|13.9 MB|23|
|3962|Technical Blogging Ebook|277|3.9 MB|99|
|3964|Telecommunications and Data Communications Handbook|832|17.3 MB|237|
|3966|25 Secrets For Faster ASP.Net|38|1.1 MB|81|
|3968|50 Ways To Avoid Find And Fix ASP.Net Performance Issues|50|1.0 MB|83|
|3970|88 C Programs|296|1.7 MB|209|
|3972|A Guide To Web Development 101|39|5.4 MB|28|
|3974|A Quick Introduction To C++|29|679.0 KB|32|
|3976|Access 2010 Quick Reference Card|3|976.8 KB|45|
|3978|Access Advanced Book|18|969.5 KB|50|
|3980|Access 2007|218|11.3 MB|41|
|3982|Advanced PHP Programming|673|10.6 MB|192|
|3984|Advanced Solutions Of Microsoft Sharepoint Server 2013|387|7.8 MB|108|
|3986|Agile Web Development With Rails|554|5.8 MB|23|
|3988|ASP.Net Database Programming Weekend Crash Course|400|2.8 MB|88|
|3990|ASP.Net Mvc4 Mobile Website Succinctly|87|2.5 MB|67|
|3992|ASP.Net Web Api Succinctly|92|1.5 MB|212|
|3994|ASP.Net Web Deployment Using Visual Studio|155|4.2 MB|102|
|3996|ASP.Net Web Pages Using The Razor Syntax|263|4.8 MB|90|
|3998|Beginners Guide To C-Sharp And The Net Micro Framework|58|1.2 MB|28|
|4000|Beginning ASP.Net In C# And VB|877|12.3 MB|152|
|4002|Beginning ASP.Net Web Pages With Web Matrix|428|10.0 MB|167|
|4004|Beginning C-Sharp Game Programming|342|2.8 MB|142|
|4006|Beginning CSS Cascading Style Sheets For Web Design|472|8.7 MB|114|
|4008|Beginning CSS For Web Design Third Edition|453|11.8 MB|111|
|4010|Beginning HTML XHTML CSS And Javascript|866|10.2 MB|225|
|4012|Beginning HTML5 And CSS3|387|8.7 MB|178|
|4014|Beginning Java Ee 6 With Glassfish 3 2nd Edition|533|6.3 MB|81|
|4016|Beginning Microsoft Word 2010|380|12.2 MB|56|
|4018|Beginning PHP 5.3|841|7.4 MB|79|
|4020|Beginning PHP 6 Apache MySQL 6 Web Development|838|8.3 MB|223|
|4022|Beginning PHP And MySQL 4th Edition|822|5.4 MB|149|
|4024|Beginning PHP And MySQL E-Commerce 2nd Edition|737|9.4 MB|174|
|4026|Beginning PHP5 Apache And MySQL Web Development|819|7.9 MB|139|
|4028|Borland C++ Builder The Complete Reference|1008|7.0 MB|72|
|4030|Build Your Own ASP.Net Website Using C-Sharp And Vb Net|183|1.7 MB|73|
|4036|Building PHP Applications With Symfony CakePHP And Zend Framework|1235|9.2 MB|178|
|4038|Building Web Apps With WordPress|459|5.0 MB|420|
|4040|Business Intelligence In Microsoft Sharepoint 2013|401|20.8 MB|110|
|4042|C Programming And Unix|646|2.8 MB|94|
|4044|C Programming Examples|12|556.0 KB|59|
|4046|C Programming Tutorial 4th Edition|410|2.5 MB|38|
|4048|C Programming Tutorial|145|1.9 MB|53|
|4050|C# 3 The Complete Reference Herbert Schildt|913|4.1 MB|111|
|4052|C-Sharp Dot Net|480|16.2 MB|47|
|4054|C# Language Specification|552|3.2 MB|70|
|4056|C# Tutorial|216|1.9 MB|97|
|4058|Cake PHP Application Development|328|5.1 MB|66|
|4060|Cloud Management With App Controller|118|7.7 MB|14|
|4062|Cms Design Using PHP And Jquery|340|8.3 MB|273|
|4064|Core Solutions Of Microsoft Share Point Server 2013|532|12.9 MB|114|
|4066|C++ A Beginners Guide 2nd Edition|541|11.9 MB|85|
|4068|C++ Amp Accelerated Massive Parallelism With Microsoft Visual C++|355|9.5 MB|123|
|4071|C++ Complete Reference 3rd Edition|1041|10.8 MB|105|
|4079|C++ For Computer Scienceand Engineering 4 Edition Book|717|8.7 MB|60|
|4085|C++ For Dummies 5th Edition|435|7.7 MB|56|
|4093|C++ For Mathematicians An Introduction For Students And Professionals|521|28.8 MB|145|
|4095|C++ Without Fear Second Edition|96|1.1 MB|145|
|4099|CSS3 For Dummies|387|8.9 MB|64|
|4101|CSS3 Foundations|354|14.2 MB|114|
|4103|CSS3 Pushing The Limits|386|11.9 MB|138|
|4105|C# Dot.Net Web Developers Guide|816|5.7 MB|103|
|4107|C# Programming|175|873.7 KB|40|
|4109|Designing Evolvable Web Apis With ASP.Net|35|4.9 MB|72|
|4111|Developing Enterprise iOS Applications|114|4.7 MB|35|
|4113|Development Of The C Language|16|533.7 KB|36|
|4115|Digital Speech Processing Using Matlab|188|10.6 MB|150|
|4117|Dreamweaver CSS5 Mobile And Web Development With HTML5 CSS3 And Jquery|284|9.9 MB|196|
|4119|Effective Web Presence Solutions For Small Businesses|353|3.4 MB|59|
|4121|Elementary Mathematical And Computational Tools For Electrical And Computer Engineers Using Matlab|349|3.3 MB|126|
|4125|Elementary Numerical Methods And C++|188|8.2 MB|65|
|4127|Embedded C Programming|421|13.5 MB|108|
|4129|Exam 77-424 Mos 2013 Study Guide For Microsoft Access|232|5.9 MB|148|
|4131|Expert C Programming|290|2.2 MB|90|
|4134|Expert PHP And MySQL|328|6.6 MB|139|
|4136|Exploring Microsoft Sharepoint 2013|250|7.4 MB|91|
|4138|Extending Microsoft Dynamics Ax 2012 Cookbook|314|12.0 MB|113|
|4140|Financial Modeling For Business Owners And Entrepreneurs|335|12.4 MB|72|
|4142|Foundation HTML5 With CSS3|424|7.6 MB|174|
|4144|Foundation Website Creation With HTML5 CSS3 And Javascript|290|5.8 MB|293|
|4146|Fundamentals Of Computer Programming With C#|1122|9.2 MB|186|
|4148|Fundamentals Of Electromagneticswith Matlab|699|8.9 MB|103|
|4150|Getting Started With Entity Framework 6 Code First Using Mvc 5|292|4.6 MB|78|
|4152|Gis For Web Developers|262|3.9 MB|55|
|4154|Google Game Plan For Success Increasing Web Presence With Google Adwords Analytics And Website Optimizer|459|9.9 MB|217|
|4156|Graphics And Animation On iOS|80|3.7 MB|90|
|4158|Guide To HTML5 And CSS3 Web Design|510|11.1 MB|391|
|4160|Hacking Exposed Web Applications|482|5.0 MB|46|
|4162|Head First C Programming|632|25.6 MB|149|
|4164|Head First HTML With CSS And XHTML|706|18.7 MB|508|
|4166|Head First Microsoft Excel|440|19.1 MB|159|
|4168|Head First WordPress|366|18.7 MB|726|
|4170|Home Networking Bible 2nd Edition|766|6.4 MB|140|
|4172|How To Do Everything With Microsoft Office Powerpoint 2007|433|8.5 MB|33|
|4174|HTML A Beginners Guide 4th Edition|539|8.0 MB|59|
|4176|HTML And CSS Design And Build Websites|514|18.8 MB|992|
|4178|HTML And CSS The Complete Reference Book|857|8.6 MB|99|
|4180|HTML Language Designing Documents For The World Wide Web|26|846.7 KB|47|
|4182|HTML Tutorial Simply Easy Learning|265|2.3 MB|54|
|4184|HTML XHTML And CSS Bible|843|21.3 MB|195|
|4188|HTML5 And CSS3 All In One For Dummies|1107|23.6 MB|221|
|4190|HTML5 Hacks|504|8.4 MB|217|
|4192|HTML5 In Action|466|11.4 MB|171|
|4194|HTML5 Iphone Web Application Development|338|7.2 MB|166|
|4196|Image Processing In C Second Edition|816|6.5 MB|64|
|4198|Implementing Data Warehouse With Microsoft SQL Server 2012|839|21.3 MB|99|
|4202|In The Beginning Was The Command Line|81|851.2 KB|16|
|4204|Inbound Marketing And Seo|362|9.8 MB|98|
|4206|Inside Microsoft Sharepoint 2013|766|10.5 MB|106|
|4208|Integrating PHP With Windows|657|12.3 MB|116|
|4210|Interactive Data Visualization For Web|186|3.0 MB|57|
|4212|Intro To ASP.Net Mvc 4 With Visual Studio Beta|118|4.4 MB|64|
|4214|Introducing ASP.Net Web Pages 2|148|3.4 MB|78|
|4216|Introducing iOS 8|333|10.7 MB|33|
|4218|Introducing Microsoft SQL Server 2014|144|7.9 MB|104|
|4220|Introduction To C# Advanced|65|822.5 KB|68|
|4222|Introduction To C#|41|137.7 KB|49|
|4224|Introduction To Fuzzy Logic Using Matlab|440|9.7 MB|210|
|4226|Introduction To Ms Word 2007|51|1.5 MB|38|
|4228|Introduction To Visual Studio And C#|48|1.5 MB|63|
|4230|iOS 4 In Action|506|8.2 MB|18|
|4232|iOS 5 Recipes|609|23.1 MB|20|
|4234|iOS 6 Recipes|684|16.7 MB|25|
|4236|iOS 7 In Action|370|11.3 MB|23|
|4238|iOS Development|342|16.8 MB|34|
|4240|iOS Game Development Cookbook|395|7.9 MB|73|
|4242|iOS In Practice|305|7.6 MB|30|
|4244|iOS Sdk Programming Beginners Guide|529|9.7 MB|28|
|4246|Javascript For PHP Developers|160|5.4 MB|149|
|4248|Jump Start HTML5|313|4.5 MB|211|
|4250|Learn Gamesalad For iOS|405|12.9 MB|28|
|4252|Learn iOS 7 App Development|772|13.5 MB|27|
|4256|Learn To Program With C++|625|7.7 MB|150|
|4258|Learning iOS 8 For Enterprise|220|7.6 MB|45|
|4260|Learning iOS Programming 2nd Edition|428|12.7 MB|22|
|4262|Learning iOS Programming 3rd Edition|452|13.5 MB|53|
|4264|Learning Kendo Ui Web Development|289|2.6 MB|73|
|4266|Learning Microsoft Windows Server 2012 Dynamic Access Control|146|3.8 MB|101|
|4268|Learning PHP Design Patterns|362|10.7 MB|70|
|4270|Learning PHP MySQL And Javascript|528|7.9 MB|110|
|4272|Learning PHP MySQL Javascript And CSS 2nd Edition|582|11.5 MB|159|
|4274|Learning PHP MySQL Javascript CSS And HTML5|729|14.1 MB|576|
|4276|Learning Three Js The Javascript 3d Library For Web Gl|402|10.7 MB|77|
|4278|Low Level C Programming|49|220.4 KB|67|
|4280|Mac Os X And iOS Internals|867|11.4 MB|83|
|4282|Mac Os X Lion Bible|866|21.7 MB|30|
|4284|Mac Os X Snow Leopard The Missing Manual|904|11.3 MB|33|
|4286|Machine Learning For Hackers|322|10.1 MB|862|
|4288|Macruby In Action|270|9.6 MB|30|
|4290|Manage Your Life With Outlook For Dummies|362|7.9 MB|36|
|4292|Mastering PHP Myadmin 3.3.X For Effective MySQL Management|412|6.5 MB|58|
|4294|Mastering PHP Myadmin 3.4 For Effective MySQL Management|394|8.5 MB|90|
|4296|Mastering Splunk|344|8.7 MB|123|
|4298|Matlab Differential Equations|178|6.0 MB|183|
|4300|Matlab Optimization Techniques|284|6.5 MB|273|
|4302|Matlab Programming For Numerical Analysis|238|9.4 MB|250|
|4304|Matrix Calculus And Kronecker Product With Applications And C++ Programs|263|13.7 MB|67|
|4306|Mcpd Exam Ref|302|2.8 MB|14|
|4308|Microsoft Access 2003 Macros Training Book|71|460.8 KB|45|
|4310|Microsoft C-Sharp Programming For The Absolute Beginner|394|12.1 MB|58|
|4312|Microsoft Dynamics Ax 2012 R2 Services|264|3.3 MB|84|
|4314|Microsoft Excel 2010 Step By Step|479|23.5 MB|62|
|4316|Microsoft Excel 2013 Step By Step|125|3.8 MB|167|
|4318|Microsoft Expression Web 4|545|25.5 MB|62|
|4320|Microsoft Frontpage 2002 Essential Web Concepts|200|1.1 MB|29|
|4322|Microsoft Mapping|170|7.6 MB|42|
|4324|Microsoft Office 365|337|15.0 MB|55|
|4326|Microsoft Office Access 2003 Step By Step|350|9.4 MB|48|
|4328|Microsoft Office Excel 2003 Programming Inside Out|589|8.2 MB|86|
|4330|Microsoft Outlook 2003 Introduction|212|3.0 MB|19|
|4332|Microsoft Outlook 2013 Step By Step|576|15.2 MB|99|
|4334|Microsoft Powerpoint 2002 Fast And Easy|365|11.9 MB|28|
|4336|Microsoft Powerpoint 2013 Step By Step|480|12.5 MB|121|
|4338|Microsoft Powerpoint Mos 2013 Study Guide|178|4.0 MB|113|
|4340|Microsoft Project 2007|146|1.5 MB|15|
|4342|Microsoft Sharepoint 2013 Administration Inside Out|954|13.1 MB|199|
|4344|Microsoft SQL Server 2012 Internals|983|13.7 MB|169|
|4346|Microsoft SQL Server 2012 With Hadoop|96|2.7 MB|100|
|4348|Microsoft System Center Configuration Manager Field Experience|92|4.9 MB|68|
|4352|Microsoft System Center Integrated Cloud Platform|80|3.0 MB|70|
|4354|Microsoft System Center Network Virtualization And Cloud Computing|94|5.0 MB|106|
|4356|Microsoft System Center Optimizing Service Manager|96|3.7 MB|73|
|4360|Microsoft Visual Basic 2013 Step By Step|690|20.9 MB|58|
|4362|Microsoft Visual C-Sharp 2013 Step By Step|824|9.6 MB|78|
|4364|Microsoft Word 2010 Training|27|1.2 MB|54|
|4366|Microsoft Word 2013 Step By Step|576|15.4 MB|128|
|4368|Migrating To Android For iOS Developers|525|10.3 MB|183|
|4370|Mobile Web Development|524|32.9 MB|36|
|4372|More iOS 6 Development|542|12.0 MB|26|
|4374|Mos 2013 Study Guide For Microsoft Powerpoint|178|3.9 MB|54|
|4376|Mos 2013 Study Guide For Microsoft Word Exam|186|3.5 MB|88|
|4378|Ms Crm 2011 Step By Step|448|20.1 MB|51|
|4380|Ms Excel 2010 Step By Step|480|23.5 MB|80|
|4382|Networking All In One Desk Reference For Dummies 2nd Edition|866|9.7 MB|30|
|4384|Networking All In One Desk Reference For Dummies 3rd Edition|914|15.6 MB|89|
|4386|Networking For Dummies 8th Edition|434|7.5 MB|102|
|4388|Object Oriented Programming In C# For C And Java Programmers|485|3.1 MB|44|
|4390|Object Oriented Programming With C|222|1.6 MB|76|
|4392|Official ISC Guide To The CSSLP CBK Second Edition|781|12.5 MB|34|
|4394|Open Data Structures In C++|336|2.9 MB|58|
|4396|Optimizing Software In C++|164|2.3 MB|106|
|4398|Oracle Database Architecture Expert 3rd Edition|823|7.7 MB|62|
|4400|Oracle Database Installation Guide For Hp-Ux Itanium|230|2.4 MB|20|
|4402|Oracle Database Java Developers Guide|286|4.2 MB|101|
|4404|Oracle Database SQL Reference 10g Release 2|1427|8.3 MB|32|
|4406|Oracle Dba Concise Handbook|92|1.1 MB|42|
|4408|Oracle Grid Infrastructure Installation Guide For Ibm Aix On Power Systems|244|2.6 MB|28|
|4410|Oracle Grid Infrastructure Installation Guide For Oracle Solaris|232|2.4 MB|33|
|4412|Oracle Streams Replication Administrators Guide|452|3.3 MB|21|
|4414|Outlook 2007 All In One Desk Reference For Dummies|842|24.4 MB|28|
|4416|Outlook 2010 All In One For Dummies|940|19.3 MB|46|
|4418|Phonegap Mobile Application Development Cookbook|320|7.8 MB|139|
|4420|PHP 6 And MySQL 6 Bible|915|17.4 MB|351|
|4422|PHP And MySQL 24 Hour Trainer|506|21.9 MB|246|
|4424|PHP And MySQL The Missing Manual 2nd Edition|548|12.4 MB|226|
|4426|PHP And MySQL The Missing Manual|498|14.7 MB|80|
|4428|PHP And MySQL Web Development 4th Edition|1009|8.6 MB|445|
|4430|PHP Application Development With Netbeans|302|8.3 MB|126|
|4432|PHP Master Write Cutting-Edge Code|404|9.6 MB|201|
|4434|PHP MySQL Javascript And HTML5 All-In-One For Dummies|724|9.6 MB|390|
|4436|PHP MySQL Novice To Ninja 5th Edition|524|11.5 MB|963|
|4438|PHP Objects Patterns And Practice 3rd Edition|537|6.2 MB|62|
|4440|PHP Objects Patterns And Practice 4th Edition|511|6.5 MB|311|
|4442|PHP5 And MySQL Bible|1083|18.8 MB|183|
|4444|Powerpoint 2007 All In One Desk Reference For Dummies|673|9.5 MB|36|
|4446|Powerpoint 2007 Just The Steps For Dummies|242|8.0 MB|25|
|4448|Powerpoint 2007|140|4.6 MB|25|
|4450|Powerpoint 2010 All In One For Dummies|604|12.8 MB|114|
|4452|Powerpoint 2010 For Dummies|340|8.1 MB|45|
|4454|Practical Apache Struts 2 Web 2 Projects|348|3.0 MB|86|
|4456|Practical C++ Programming 1995|549|3.8 MB|41|
|4458|Practical C++ Programming Teacher Guide|79|766.7 KB|70|
|4460|Practical Web 2.0 Applications With PHP|592|5.2 MB|142|
|4462|Practical Web Technologies|498|3.5 MB|32|
|4464|Pro CSS For High Traffic Websites|423|8.5 MB|68|
|4466|Pro HTML5 Accessibility|381|7.4 MB|141|
|4468|Pro HTML5 And CSS3 Design Patterns|514|7.5 MB|289|
|4470|Pro iOS Continuous Integration|214|6.9 MB|85|
|4472|Pro iOS Geo|322|14.1 MB|36|
|4474|Pro iOS Web Design And Development|486|12.1 MB|74|
|4476|Pro Opengl Es For iOS|362|7.8 MB|41|
|4478|Pro Oracle Spatial For Oracle Database 11g|819|12.7 MB|67|
|4480|Pro Oracle SQL|595|4.5 MB|108|
|4482|Pro PHP And Jquery|394|8.1 MB|341|
|4484|Pro PHP Application Performance|254|10.5 MB|180|
|4486|Pro Visual C++ Cli And The .Net 2.0 Platform|961|19.6 MB|82|
|4488|Problems And Solutions In Scientific Computing With C++ And Java Simulations|432|10.5 MB|282|
|4492|Professional iOS Database Application Programming 2nd Edition|388|12.3 MB|53|
|4494|Professional iOS Network Programming|364|10.4 MB|51|
|4496|Programming Abstractions In C++|682|9.4 MB|75|
|4498|Programming ASP.Net Mvc 4|492|7.8 MB|81|
|4500|Programming In C Unix System Calls And Subroutines Using C|847|2.8 MB|79|
|4502|Programming iOS 4 Cookbook|640|7.6 MB|19|
|4504|Programming iOS 5 Cookbook|900|14.4 MB|19|
|4526|Programming iOS 5|1014|10.6 MB|22|
|4528|Programming iOS 6|1185|12.7 MB|22|
|4530|Programming iOS 7 Cookbook|1055|16.7 MB|36|
|4532|Programming iOS 7 Fundamentals|422|7.7 MB|47|
|4534|Programming Microsoft Asp.Net Mvc 3rd Edition Book|516|7.8 MB|187|
|4536|Python Web Development With Django|405|2.8 MB|302|
|4538|Query And Javascript|382|2.0 MB|103|
|4540|Rapidweaver 5|362|13.6 MB|10|
|4542|Realtime Web Apps|299|7.0 MB|79|
|4544|Reporting With Microsoft SQL Server 2012|143|3.7 MB|91|
|4546|Sams Teach Yourself Core Data For Mac And iOS In 24 Hours 2nd Edition|480|13.2 MB|96|
|4548|Sams Teach Yourself Mac Os X Lion In 10 Minutes|241|5.8 MB|57|
|4550|Sams Teach Yourself PHP MySQL And Apache All In One 5th Edition|671|8.0 MB|419|
|4552|Search Engine Optimization An Hour A Day Second Edition|387|8.9 MB|106|
|4554|Search Engine Optimization Your Visual Blueprint For Effective Internet Marketing 2nd Edition|340|16.3 MB|78|
|4556|Search Marketing Benchmark Guide|275|7.1 MB|55|
|4558|Selenium Webdriver Practical Guide|264|5.6 MB|282|
|4560|SEO Bible|409|7.9 MB|106|
|4562|SEO Made Simple Wordtrackers Free Seo Guide|107|6.2 MB|68|
|4564|SEO Search Engine Optimization Secrets|537|8.8 MB|133|
|4566|Seven Web Frameworks In Seven Weeks|296|2.7 MB|134|
|4568|Signalr Programming In Microsoft Asp.Net|279|7.0 MB|144|
|4570|Spring Web Services 2 Cookbook|322|3.8 MB|286|
|4572|SQL Server 2014 Development Essentials|213|3.2 MB|80|
|4574|Stunning CSS3|320|7.8 MB|422|
|4576|Switching To The Mac The Missing Manual Mountain Lion Edition|764|18.6 MB|35|
|4578|Switching To The Mac The Missing Manual Snow Leopard Edition|658|9.0 MB|34|
|4580|SWO Warrior|496|7.8 MB|12|
|4582|Teach Yourself Borland C++ Builder In 21 Days|536|5.5 MB|100|
|4584|Teach Yourself C++ In 21 Days 2nd Edition|772|2.3 MB|61|
|4586|Teach Yourself Oracle 8 In 21 Days|734|6.6 MB|30|
|4588|Teach Yourself Visually Microsoft Excel 2010|352|84.5 MB|210|
|4590|Teach Yourself Visually Microsoft Powerpoint 2013|354|37.5 MB|113|
|4592|Testing Umts|260|4.4 MB|10|
|4594|The Art and Science of CSS|225|10.4 MB|84|
|4596|The Art Of Seo Mastering Search Engine Optimization 3rd Edition Ebook|984|22.0 MB|4245|
|4600|The Basics Web Hacking|179|4.4 MB|115|
|4602|The Book Of CSS3 2nd Edition|306|8.0 MB|388|
|4604|The Book Of IMAP|356|3.8 MB|27|
|4606|The Book Of Pf A No-Nonsense Guide To The Openbsd Firewall|188|6.7 MB|35|
|4608|The Business Of Android Apps Development 2nd Edition Ebook|162|3.7 MB|114|
|4610|The Business Of iOS App Development 3rd Edition|433|12.1 MB|93|
|4612|The C Book|359|1.7 MB|15|
|4614|The C Programming Language|288|22.7 MB|326|
|4616|The Comsoc Guide To Passive Optical Networks Book|194|1.8 MB|26|
|4618|The Core iOS Developers Cookbook 5th Edition|672|7.2 MB|81|
|4620|The C++ Programming Language 4th Edition|1361|4.2 MB|355|
|4622|The C++ Programming Language Third Edition|957|4.4 MB|82|
|4624|The CSS3 Anthology 4th Edition|441|12.3 MB|316|
|4626|The CUDA Handbook|522|2.3 MB|44|
|4630|The Definitive Guide to HTML5 Video|337|9.3 MB|175|
|4632|The Entity Framework 4 And ASP.Net Web Forms|255|4.9 MB|119|
|4634|The Essential Guide to Serial ATA and SATA Express|491|6.4 MB|157|
|4636|The Facebook Marketing Book|284|9.3 MB|207|
|4638|The Game Believes In You How Digital Play Can Make Our Kids Smarter|212|2.3 MB|61|
|4640|The Game Makers Companion|443|13.2 MB|101|
|4642|The Intel Microprocessors, 8th Edition|944|6.2 MB|22|
|4644|The iPhone Book, 5th Edition|369|16.4 MB|39|
|4646|The Modern Web|266|5.3 MB|82|
|4648|The Network Security Test Lab|482|18.5 MB|1394|
|4650|The New Community Rules|368|13.9 MB|52|
|4652|The Social Media Marketing Book|241|5.8 MB|160|
|4654|The TINI Specification and Developers Guide|382|1.3 MB|33|
|4656|Theory of Fun for Game Design, 2nd Edition|299|30.5 MB|85|
|4658|Thinking In C#|957|5.1 MB|167|
|4660|Threading In C#|125|1.5 MB|139|
|4662|Torque 3d Game Development Cookbook|381|4.5 MB|62|
|4664|Training Guide Configuring Advanced Windows Server 2012 R2 Services|753|18.6 MB|156|
|4666|Transportation Management with SAP TM 9|318|14.3 MB|127|
|4668|Troubleshooting Ubuntu Server|259|7.4 MB|91|
|4672|TypePad For Dummies|435|10.0 MB|9|
|4675|U.X.L Graphic Novelists Volume 1|250|14.6 MB|51|
|4678|Ubuntu 7.10 Linux Unleashed|841|8.7 MB|97|
|4682|Ubuntu NetBooks|259|8.4 MB|99|
|4684|Ubuntu Unleashed 2015 Edition, 10th Edition|913|8.5 MB|297|
|4686|Ultra Wideband Systems With Mimo Book|274|2.9 MB|24|
|4688|Umts Networks And Beyond|363|4.3 MB|66|
|4690|Umts Performance Measurement|228|4.2 MB|23|
|4692|UMTS Radio Network Planning, Optimization and QoS Management|343|5.1 MB|109|
|4694|Umts Security Book|288|2.3 MB|367|
|4696|Umts Signaling 2nd Edition Book|169|2.5 MB|41|
|4698|Understanding Ipv6 3rd Edition Book|715|5.4 MB|28|
|4700|Understanding Lte And Its Performance|277|4.7 MB|49|
|4702|Understanding Lte With Matlab|510|8.7 MB|512|
|4704|Unity 2D Game Development Cookbook|256|8.4 MB|403|
|4706|Unity 2d Game Development|126|2.1 MB|304|
|4708|Unity 3.X Scripting Ebook|291|4.6 MB|83|
|4710|Unity 3D UI Essentials|280|6.3 MB|455|
|4712|Unity 4 Game Development|693|8.1 MB|164|
|4714|Unity 4.x Cookbook|386|5.3 MB|52|
|4717|Unity 4.X Game Ai Programming|232|3.4 MB|185|
|4719|Unity 5 For Android Essentials Ebook|200|3.0 MB|574|
|4721|Unity 5 From Zero To Proficiency|162|3.6 MB|1225|
|4723|Unity 5 Game Optimization|419|5.3 MB|889|
|4725|Unity AI Programming Essentials|162|4.8 MB|505|
|4727|Unity Animation Essentials|200|9.0 MB|407|
|4729|Unity Character Animation With Mecanim|380|5.9 MB|462|
|4731|Unity for Absolute Beginners|598|28.4 MB|655|
|4733|Unity Game Development Blueprints|318|12.2 MB|288|
|4735|Unity Game Development Scripting|202|2.7 MB|597|
|4737|Unity iOS Game Development Beginners Guide|314|12.7 MB|103|
|4739|Unity iOS Game Development|314|12.0 MB|214|
|4741|Unity Shaders and Effects Cookbook|268|5.7 MB|309|
|4743|Unreal Development Kit Game Design Cookbook|544|14.4 MB|160|
|4745|Unreal Engine Physics Essentials|353|10.5 MB|200|
|4747|Unrealscript Game Programming Cookbook|272|6.2 MB|133|
|4749|Untangle Network Security|368|8.2 MB|634|
|4751|Upgrading and Fixing Computers Do it Yourself For Dummies|340|6.5 MB|23|
|4753|USB Complete, 3rd Edition|593|4.8 MB|27|
|4755|Using Autocad 2011|1169|22.9 MB|66|
|4757|Using Scribe Insight|133|5.8 MB|27|
|4759|Using Yocto Project with BeagleBone Black|144|1.3 MB|213|
|4761|UWB Communication Systems A Comprehensive Overview|507|15.4 MB|18|
|4763|UXL Graphic Novelists Volume 3|208|11.9 MB|24|
|4765|VHDL for Logic Synthesis, 3rd Edition|466|2.7 MB|13|
|4767|Video And Multimedia Transmissions Over Cellular Networks|413|7.8 MB|175|
|4769|Visio 2007 Introduction|70|1.4 MB|11|
|4771|Visual C# Programming Basics|19|1,009.0 KB|128|
|4773|Visual C# 2008 Step by Step Book|673|9.6 MB|116|
|4775|Visual Quick Start Guide CSS3|457|12.0 MB|80|
|4777|VMware Horizon 6 Desktop Virtualization Solutions|362|10.9 MB|25|
|4779|VMware Horizon View 6.0 Desktop Virtualization Cookbook|699|8.3 MB|55|
|4781|VMware Virtual San Cookbook|208|5.6 MB|66|
|4783|VMware vSphere 4 Implementation|689|17.1 MB|23|
|4785|WCDMA For UMTS 3rd Edition Book|481|7.8 MB|12|
|4787|WCDMA UMTS Deployment Handbook|416|3.8 MB|22|
|4789|WCF 4.5 Multi-Layer Services Development with Entity Framework, 3rd Edition|394|9.1 MB|93|
|4792|We The Media Ebook|312|1.6 MB|15|
|4795|Web Application Development With R Using Shiny|110|1.9 MB|531|
|4797|Web Application Security|513|4.6 MB|74|
|4799|Web PeNetration Testing With Kali Linux|342|17.4 MB|270|
|4801|Web Technologies|591|4.4 MB|75|
|4803|WebGL Game Development|418|5.1 MB|114|
|4805|Wideband Beamforming Concepts and Techniques|304|19.6 MB|44|
|4807|Wikis For Dummies|337|6.9 MB|16|
|4809|WildFly Cookbook - Deploy and Manage Java Based Applications Using Wildfly - Networking Book|604|10.2 MB|350|
|4811|Wimax Security And Quality Of Service Book|425|4.1 MB|450|
|4813|Windows 8 and Office 2013 For Dummies Portable Edition|482|9.4 MB|28|
|4815|Windows 8 and Windows Phone 8 Game Development|499|6.1 MB|50|
|4817|Windows Forms Programming With C-Sharp|755|7.7 MB|49|
|4819|Windows Mobile Game Development|468|3.3 MB|77|
|4821|Windows Phone 7 Game Development|593|7.7 MB|41|
|4823|Windows Software Compatibility and Hardware Troubleshooting|117|3.9 MB|128|
|4825|Wireless And Mobile Networks Security|689|8.6 MB|51|
|4827|Wireless Network Security A Beginners Guide|369|20.4 MB|153|
|4829|Wireless Transceiver Circuits|572|14.9 MB|181|
|4831|Wireshark Essentials Book|194|3.7 MB|152|
|4833|Wireshark Starter Book|68|2.9 MB|42|
|4835|Word 2013 eLearning Kit For Dummies|349|15.9 MB|110|
|4837|WordPress 2.7 Cookbook|316|9.3 MB|181|
|4839|Working Together Apart- Collaboration Over The Internet Book|153|2.2 MB|36|
|4841|XMPP The Definitive Guide Book|307|2.9 MB|92|
|4843|XNA 3d Primer Ebook|42|923.5 KB|11|
|4845|XNA 4.0 Game Development By Example|428|6.0 MB|106|
|4847|XNA Game Studio 4.0 Programming|526|6.2 MB|59|
|4849|ZBrush 4 Sculpting for Games Beginners Guide|348|11.4 MB|232|
|4851|Zenoss Core Network and System Monitoring|276|8.7 MB|36|
|4853|Access 2003 Bible Ebook|638|25.2 MB|71|
|4857|Access 2013 For Dummies|459|13.0 MB|124|
|4859|Access 2013 The Missing Manual|867|22.2 MB|133|
|4861|Access Data Analysis Cook Book|368|8.7 MB|110|
|4865|Access Vba Programming For Dummies|407|6.7 MB|150|
|4867|Administering Windows Server 2012 Exam 70-411|714|31.8 MB|66|
|4869|Advanced Joomla|396|8.7 MB|96|
|4871|Backtrack Oracle Tutorial Book|19|1,000.3 KB|33|
|4873|Beginning Joomla|494|14.2 MB|62|
|4875|Building Job Sites With Joomla|236|6.4 MB|75|
|4877|Building Websites With Joomla 1.5|380|13.0 MB|62|
|4879|Building Websites With Joomla|340|8.5 MB|83|
|4881|Creating A Grade Sheet With Microsoft Excel|17|178.5 KB|40|
|4883|Drupal 7 Bible|486|51.1 MB|270|
|4885|Excel 2007 Advanced|159|4.8 MB|51|
|4887|Excel 2007 Training Excel Quick Reference Card|3|185.2 KB|35|
|4889|Foundation Joomla|478|11.1 MB|45|
|4891|Head First Pmp 2nd Edition|812|29.2 MB|31|
|4893|Joomla 1.5 Development Cookbook|359|4.1 MB|39|
|4895|Joomla 1.5 Javascript Jquery|292|3.0 MB|115|
|4897|Joomla 1.5 Multimedia|375|12.6 MB|31|
|4899|Joomla 1.5 Site Blueprints|249|9.8 MB|29|
|4901|Joomla 1.5 Template Design|283|8.8 MB|28|
|4903|Joomla 1.5 Templates Cookbook|236|6.1 MB|34|
|4905|Joomla 1.5 Top Extensions Cookbook|445|24.0 MB|33|
|4907|Joomla 1.5x Customization|288|3.4 MB|31|
|4909|Joomla 3 Template Essentials|142|2.8 MB|104|
|4911|Joomla Bible|794|20.7 MB|123|
|4913|Joomla Second Edition|385|9.1 MB|50|
|4915|Linking Oracle Tables To Microsoft Access|15|131.1 KB|59|
|4917|Microsoft Access 2010 Vba Macro Programming|400|2.0 MB|161|
|4919|Microsoft Access 2013 Academic Course|530|28.3 MB|138|
|4921|Microsoft Access 2013 Complete Book|597|58.5 MB|188|
|4923|Microsoft Dynamics Crm 2011 Cookbook|396|6.8 MB|79|
|4925|Microsoft Dynamics Crm 2011 Reporting|300|10.0 MB|82|
|4927|Microsoft Dynamics Gp 2013 Cookbook|340|4.7 MB|68|
|4929|Microsoft Excel 2002 Vba|89|437.0 KB|49|
|4931|Microsoft Excel 2007 Shortcut And Function Keys|20|367.5 KB|34|
|4933|Microsoft Excel 2013 Data Analysis And Business Modeling|889|21.5 MB|244|
|4935|Microsoft Exchange Server 2013 Inside Out Mailbox And High Availability|854|15.7 MB|69|
|4937|Microsoft Office Access 2003 The Complete Reference|753|6.8 MB|84|
|4939|Microsoft Office Access 2007 All In One Desk Reference For Dummies|766|16.2 MB|74|
|4941|Microsoft Sharepoint 2010 Performancepoint Services Unleashed|342|11.7 MB|36|
|4943|Microsoft Sql Server 2012 Integration Services|801|16.4 MB|145|
|4945|Microsoft Windows Powershell Programming For The Absolute Beginner|377|2.8 MB|694|
|4947|Ms Excel 2007 Introduction|136|5.0 MB|32|
|4949|Oracle Data Mining Concepts|138|1.0 MB|33|
|4951|Oracle Database 2 Day Real Application Clusters Guide|240|1.6 MB|26|
|4953|Oracle Database 2 Day Security Guide|120|1.1 MB|23|
|4955|Oracle Database Data Cartridge Developers Guide|374|3.0 MB|18|
|4957|Oracle Database Gateway For Appc|216|1.5 MB|18|
|4959|Oracle Database Gateway For Informix|76|813.5 KB|17|
|4961|Oracle Database Gateway For Sybase|78|822.7 KB|18|
|4963|Oracle Database Gateway For Teradata|76|780.7 KB|16|
|4965|Oracle Database Gateway For Websphere Mq|118|1.1 MB|21|
|4967|Oracle Database Gateway Installation And Configuration Guide For Windows|182|962.9 KB|38|
|4969|Oracle Database Gateway Installation And Configuration Guidefor Linux|206|1.0 MB|69|
|4971|Oracle Database Net Services Administrators Guide|320|1.5 MB|29|
|4973|Oracle Database Net Services Reference|232|901.4 KB|24|
|4977|Oracle Database Securefiles And Large Objects Developers Guide|428|3.3 MB|20|
|4979|Oracle Database Sqlj Developers Guide|504|2.6 MB|22|
|4981|Oracle Database Upgrade Guide|252|2.9 MB|33|
|4983|Oracle Database Xml C++ API Reference|196|684.0 KB|133|
|4985|Oracle Multimedia Dicom Developers Guide|378|1.9 MB|23|
|4987|Oracle Multimedia Reference|512|1.9 MB|22|
|4989|Oracle Multimedia Users Guide|240|1.5 MB|21|
|4991|Oracle Olap Customizing Analytic Workspace Manager|76|899.3 KB|27|
|4993|Oracle Streams Extended Examples|174|866.8 KB|25|
|4995|Oracle Text Application Developers Guide|256|2.7 MB|20|
|4997|Oracle Text Reference|719|9.2 MB|25|
|4999|Oracle Timesten In Memory Database Java Developers Guide|110|1.4 MB|77|
|5001|Oracle Timesten In Memory Database Troubleshooting Guide|124|1.5 MB|25|
|5003|Oracle Xml Developers Kit Programmers Guide|660|3.3 MB|61|
|5005|Using Microsoft Excel And Access 2013 For Accounting|386|18.3 MB|311|
|5007|Using Microsoft Excel For Graphical Analysis|7|185.3 KB|156|
|5009|Windows 8 For Dummies Quick Reference|267|9.0 MB|27|
|5011|Word 2007 Advanced|145|3.8 MB|51|
|5013|Word 2007 Introduction|119|4.0 MB|36|
|5015|WordPress Theme Development 3rd Edition|245|8.4 MB|451|
|5018|Accelerated Dom Scripting With Ajax Apis And Libraries|243|3.1 MB|76|
|5020|Adding Ajax - Making Existing Sites More Interactive|401|3.8 MB|97|
|5022|Ajax And PHP|285|3.9 MB|225|
|5024|Ajax For Dummies|382|5.3 MB|126|
|5028|Android For The Beaglebone Black|197|2.8 MB|148|
|5030|Android Fragments|131|1.0 MB|129|
|5032|Android Quick Apis Reference|270|1.7 MB|160|
|5034|Android Recipes 3rd Edition|760|4.7 MB|91|
|5036|Android Security Internals|434|4.3 MB|157|
|5040|Beginning Ajax With Asp.Net|429|9.3 MB|128|
|5042|Beginning Ajax With PHP|270|3.1 MB|391|
|5044|Beginning Android 3d Game Development|482|6.9 MB|252|
|5046|Beginning Java 8 Apis Extensions And Libraries|796|7.7 MB|280|
|5048|Beginning Java 8 Fundamentals|810|6.0 MB|575|
|5052|Beginning Javascript With Dom Scripting And Ajax 2nd Edition|377|4.7 MB|301|
|5054|Beginning PHP And Postgre SQL 8|863|4.4 MB|92|
|5056|Beginning Python|641|12.3 MB|218|
|5058|Beginning Smartphone Web Development|366|7.4 MB|95|
|5060|Build Your Own Ajax Web Applications|320|2.9 MB|227|
|5062|Build Your Own Database Driven Web Site Using PHP MySQL 4th Edition|507|5.7 MB|307|
|5066|Cocos2d-X Andriod Game Development Essentials|137|3.0 MB|84|
|5068|Codeigniter For Rapid PHP Application Development|257|2.9 MB|207|
|5070|Delphi Andriod Cookbook|329|8.7 MB|66|
|5072|Exploring Se For Android|379|3.2 MB|91|
|5074|Foundations Of Agile Python Development|417|5.4 MB|147|
|5076|Foundations Of Ajax|297|4.9 MB|129|
|5078|Foundations Of Asp.Net Ajax|288|5.2 MB|117|
|5080|Foundations Of Python Network Programming 2nd Edition|370|2.8 MB|127|
|5082|Foundations Of Python Network Programming 3rd Edition|369|2.7 MB|295|
|5084|Gui Design For Android Apps|147|5.1 MB|173|
|5086|Gwt In Action|631|8.4 MB|11|
|5088|Head First Javascript Programming|704|33.3 MB|396|
|5090|Head First Programming|442|11.7 MB|33|
|5092|Hello App Inventor Android Programming|361|17.2 MB|247|
|5094|Integrating PHP Projects With Jenkins|54|2.3 MB|112|
|5096|Java 8 Recipes 2nd Edition|627|5.2 MB|330|
|5098|Java Elearning Kit For Dummies|446|7.1 MB|111|
|5100|Java Programming Interviews Exposed|386|4.6 MB|113|
|5102|Java Se 8 For The Really Impatient|238|7.7 MB|189|
|5104|Javascript Creativity|171|2.3 MB|135|
|5106|Javascript Jquery 3rd Edition|686|10.4 MB|424|
|5108|Javaserver Faces Introduction By Example|345|4.0 MB|171|
|5110|Joomla Cash For Joomla Website|180|6.0 MB|39|
|5112|Joomla For Dummies 1st Edition|364|15.0 MB|47|
|5114|Joomla For Dummies 2nd Edition|364|17.9 MB|171|
|5116|Joomla For Dummies|345|12.0 MB|38|
|5118|Joomla Mobile Development Beginner Guide|270|5.5 MB|88|
|5120|Joomla Template Design|227|6.8 MB|65|
|5122|Joomla Templates|361|7.1 MB|99|
|5124|Joomla Virtuemart Theme And Template Design|361|5.6 MB|44|
|5126|Joomla Web Security|251|2.7 MB|88|
|5128|Kindle Fire App Development Essentials|57|3.0 MB|11|
|5130|Lean Software Development|24|2.0 MB|87|
|5132|Learn Cocos2d 2|532|7.8 MB|18|
|5134|Learn Html5|360|19.7 MB|263|
|5136|Learn Java For Android Development 3rd Edition|1190|5.7 MB|367|
|5138|Learn Java For Web Development|461|11.7 MB|199|
|5140|Learning Android 2nd Edition|288|4.9 MB|90|
|5142|Learning Android|268|3.6 MB|67|
|5144|Learning Angularjs Animations|182|2.1 MB|103|
|5146|Learning Asp.Net 3.5 2nd Edition|609|12.5 MB|64|
|5148|Learning Drupal 6 Module Development|328|4.9 MB|39|
|5152|Learning Joomla Extension Development|171|3.2 MB|39|
|5154|Learning PHP 5|398|1.5 MB|41|
|5156|Maintaining States In PHP - PHP Lecture 11|37|875.5 KB|45|
|5158|Making Use Of Python|416|3.5 MB|193|
|5160|Master Pages Themes Navigation And Site Navigation - Asp.Net Lecture 9|35|1.2 MB|42|
|5162|Mastering Dojo|545|4.2 MB|26|
|5164|Mastering Joomla 15 Extension And Framework Development|560|10.8 MB|63|
|5166|Mastering Magento Theme Design|309|9.4 MB|435|
|5168|Mastering Object Oriented Python|634|2.7 MB|381|
|5170|Metro Revealed Building Windows 8 Apps With Html5 And Javascript|103|1.9 MB|105|
|5172|Microsoft Dino Esposito Asp.Net And Ajax Architecting Webapplications|344|2.2 MB|147|
|5174|Migrating To Swift From Android|254|6.1 MB|57|
|5180|Mootools Essentials|275|1.3 MB|12|
|5182|Multi-Tier Web Applications - Asp.Net Lecture 12|8|666.3 KB|65|
|5184|No Frills Magento Layout|164|2.1 MB|389|
|5186|Object Oriented Programming  Using C++ Structures And Classes - C++ Lecture 3|46|1.0 MB|28|
|5188|Object Oriented Programming Using C++ Abstract Classes - C++ Lecture 18|25|682.6 KB|21|
|5190|Object Oriented Programming Using C++ Aggregation Vs Inheritance - C++ Lecture 20|10|656.1 KB|21|
|5192|Object Oriented Programming Using C++ Class Templates - C++ Lecture 22|17|685.6 KB|22|
|5194|Object Oriented Programming Using C++ Classes Contd - C++ Lecture 4|11|571.9 KB|22|
|5198|Object Oriented Programming Using C++ Classes Contd - C++ Lecture 6|23|741.8 KB|23|
|5200|Object Oriented Programming Using C++ Classes Contd - C++ Lecture 7|14|617.1 KB|23|
|5202|Object Oriented Programming Using C++ Dma And Classes Strings - C++ Lecture 8|50|1.2 MB|22|
|5204|Object Oriented Programming Using C++ Exception Handling - C++ Lecture 19|43|961.8 KB|21|
|5206|Object Oriented Programming Using C++ File Handling - C++ Lecture 23|44|994.3 KB|26|
|5208|Object Oriented Programming Using C++ Inheritance - C++ Lecture 13|16|736.7 KB|23|
|5210|Object Oriented Programming Using C++ Inheritance Contd - C++ Lecture 14|34|883.3 KB|22|
|5212|Object Oriented Programming Using C++ Inheritance Contd - C++ Lecture 15|13|638.0 KB|22|
|5214|Object Oriented Programming Using C++ Operator Overloading - C++ Lecture 10|23|654.6 KB|22|
|5216|Object Oriented Programming Using C++ Operator Overloading Contd - C++ Lecture 11|10|1.0 MB|23|
|5218|Object Oriented Programming Using C++ Operator Overloading Contd - C++ Lecture 12|35|917.2 KB|24|
|5220|Object Oriented Programming Using C++ Polymorphism - C++ Lecture 16|20|686.1 KB|28|
|5222|Object Oriented Programming Using C++ Polymorphism - C++ Lecture 17|25|762.8 KB|28|
|5224|Object Oriented Programming Using C++ Templates - C++ Lecture 21|14|711.6 KB|29|
|5226|Object Oriented Programming With PHP 5|267|3.0 MB|226|
|5228|Opa Up And Running|164|6.2 MB|15|
|5230|Open Data Structure In Java|334|2.3 MB|64|
|5232|Operators In Java - Java Lecture 3|31|761.2 KB|37|
|5234|Oracle Application Express Installation Guide For Oracle Database 12|86|1.2 MB|28|
|5236|Oracle Application Express Release Notes For Oracle Database 12|27|977.4 KB|23|
|5238|Oracle Database 2 Day Application Express Developer Guide|84|1.8 MB|28|
|5240|Oracle Database 2 Day Java Developer Guide|140|3.0 MB|117|
|5246|Oracle Database Advanced Queuing User Guide|524|4.1 MB|31|
|5248|Oracle Database Advanced Security Guide|220|2.1 MB|43|
|5250|Oracle Database Backup And Recovery Reference|528|4.9 MB|40|
|5252|Oracle Database Backup And Recovery User Guide|700|5.6 MB|56|
|5254|Oracle Database Client Installation Guide|84|799.0 KB|29|
|5256|Oracle Database Data Cartridge Developer Guide|374|3.8 MB|19|
|5258|Oracle Database Gateway For Appc User Guide|216|2.2 MB|17|
|5260|Oracle Database Gateway For Drda User Guide|118|1.6 MB|18|
|5262|Oracle Database Gateway For Informix User Guide|76|1.5 MB|19|
|5264|Oracle Database Gateway For Odbc User Guide|54|1.1 MB|28|
|5266|Oracle Database Gateway For SQL Server User Guide|84|1.5 MB|46|
|5268|Oracle Database Gateway For Sybase User Guide|78|1.5 MB|22|
|5270|Oracle Database Gateway For Teradata User Guide|76|1.5 MB|25|
|5272|Oracle Database New Features Guide|140|1.7 MB|40|
|5274|Oracle Database Pl SQL Language Reference|788|4.2 MB|76|
|5276|Oracle Database Readme|96|1.3 MB|31|
|5278|Oracle Database Secure Files And Large Objects Developer Guide|428|4.8 MB|44|
|5280|Oracle Real Application Clusters Administration And Deployment Guide|456|5.7 MB|72|
|5282|Oracle Universal Connection Pool For Jdbc Developer Guide|92|1.1 MB|35|
|5284|PHP 5 E-Commerce Development|357|3.3 MB|329|
|5286|PHP 5 Recipes|673|5.3 MB|143|
|5288|PHP And MySQL Affair - PHP Lecture 9|29|742.8 KB|72|
|5290|PHP And MySQL For Dummies 4th Edition|460|5.0 MB|290|
|5292|PHP And MySQL Integration - PHP Lecture 10|17|664.3 KB|80|
|5294|PHP Form And File Handling - PHP Lecture 8|30|746.5 KB|98|
|5296|PHP In A Nutshell|372|2.8 MB|101|
|5298|PHP Programming With Pear|290|2.2 MB|78|
|5300|PHP Team Development|184|1.8 MB|108|
|5302|PHP Web Services|117|6.0 MB|191|
|5306|Picture Yourself Building A Website With Joomla 16|320|5.7 MB|81|
|5308|Planning And Managing Drupal Projects|96|3.4 MB|109|
|5310|Practical Cake PHP Projects|389|3.7 MB|132|
|5312|Pro Android Python With Sl4a|296|5.3 MB|319|
|5314|Pro Drupal 7 Development Third Edition|721|9.2 MB|105|
|5316|Pro Drupal 7 For Windows Developers|443|10.5 MB|95|
|5318|Pro Java Fx 8|604|8.8 MB|1406|
|5320|Pro Javascript Development|454|5.8 MB|232|
|5322|Pro Jsf And Ajax|465|11.3 MB|89|
|5324|Pro PHP Security 2nd Edition|369|3.0 MB|258|
|5326|Pro Python 2nd Edition|369|5.5 MB|242|
|5328|Pro Typescript|233|3.6 MB|129|
|5330|Professional Ajax 2nd Edition|627|4.0 MB|457|
|5332|Professional Java For Web Applications|938|10.7 MB|907|
|5334|Professional Mobile Web Development With WordPress Joomla And Drupal|524|31.9 MB|413|
|5336|Programming Asp.Net Ajax|475|6.5 MB|142|
|5338|Programming Google Glass The Mirror Api|128|2.8 MB|84|
|5340|Programming Ground Up Booksize|326|2.2 MB|14|
|5342|Python 3 For Absolute Beginners|314|2.0 MB|370|
|5344|Python 3 Text Processing With Nltk 3 Cookbook|304|1.7 MB|147|
|5346|Python Algorithms 2nd Edition|303|3.9 MB|426|
|5348|Python Algorithms|337|3.3 MB|179|
|5350|Python And Hdf5|152|4.0 MB|207|
|5352|Python For Google App Engine|198|2.7 MB|266|
|5354|Python Penetration Testing Essentials|178|3.3 MB|235|
|5356|Regular Expression For Perl Buby PHP Python C Java And Dotnet Second Edition|127|929.9 KB|363|
|5358|Responsive Theming For Drupal|77|4.7 MB|82|
|5360|Restful Web Apis|404|7.6 MB|102|
|5362|Sams Teach Yourself Drupal In 24 Hours|457|17.0 MB|263|
|5364|Sams Teach Yourself Html5 In 10 Minutes 5th Edition|241|3.0 MB|466|
|5366|Sams Teach Yourself Html5 Mobile Application Development In 24 Hours|491|6.6 MB|518|
|5370|Selling Online With Drupal Ecommerce|264|7.3 MB|96|
|5372|Service Oriented Solutions With PHP And Bpel|313|3.3 MB|59|
|5374|Sockets And Network Programming - Java Lecture 24|20|745.9 KB|52|
|5376|The Android Developer Cookbook 2nd Edition|463|4.2 MB|200|
|5378|The Android Developer Cookbook|355|4.1 MB|110|
|5380|The Definitive Guide To Drupal 7|1077|17.1 MB|206|
|5382|The Definitive Guide To Magento|329|4.7 MB|367|
|5388|The Official Joomla Book|362|6.5 MB|202|
|5390|The PHP Anthology Volume 1|398|3.9 MB|143|
|5392|The Python Standard Library By Example|1343|5.5 MB|604|
|5394|Top 10 Benefits Of Magento Ecommerce|19|2.1 MB|153|
|5396|Using Drupal|494|10.8 MB|207|
|5398|Using Joomla|412|9.2 MB|175|
|5400|Using Multiple Classes In Java Program|4|646.0 KB|80|
|5402|Web App Testing Using Knockout Js|154|1.6 MB|54|
|5404|Web Services Technology - Asp.Net Lecture 11|25|1.8 MB|75|
|5406|Wicked Cool PHP|216|3.6 MB|198|
|5408|Windows 8 Apps Revealed Using Html5 And Javascript|139|3.2 MB|139|
|5410|Windows Powershell For Developers|85|2.9 MB|235|
|5412|Xamarin Cross Platform Application Development 2nd Edition|462|8.0 MB|258|
|5414|Xamarin Essentials Develop Android And Ios|234|3.3 MB|214|
|5448|A Crash Course From C++ To Java|29|760.3 KB|80|
|5450|A Crash Course In C++|42|324.6 KB|45|
|5452|A First Book Of C++ 4th Edition|802|39.1 MB|804|
|5454|A Practical Guide To Fedora And Red Hat Enterprise Linux 6th Edition|1321|11.3 MB|101|
|5456|A Short Course On C++|23|493.2 KB|45|
|5460|A Tutorial On Pointers And Arrays In C|53|176.4 KB|175|
|5462|A Tutorial On Socket Programming In Java|28|321.0 KB|70|
|5464|Accelerated C++ Practical Programming By Example|387|2.1 MB|415|
|5466|Acuity Color System Color Management|485|17.0 MB|21|
|5468|Ada Programming|410|1.9 MB|13|
|5470|Advanced Microsoft Excel 2013|84|7.6 MB|106|
|5472|Advanced Microsoft Word 2011 For Mac|24|2.0 MB|34|
|5474|Advanced Powerpoint 2010|16|610.0 KB|35|
|5478|Agile Principles Patterns And Practices In C#|944|9.1 MB|384|
|5483|Agile Web Development With Rails Fourth Edition|789|8.1 MB|52|
|5487|Agile Web Development With Rails Second Edition|715|5.7 MB|31|
|5490|Ajax Rich Internet Applications And Web Development For Programmers|1025|24.4 MB|354|
|5492|Algorithms And Networking For Computer Games|282|1.3 MB|108|
|5494|An Introduction To C++ Template Programming|23|316.0 KB|61|
|5496|An Introduction To Haskell Through Example Write A Scheme In 48 Hrs|138|1.6 MB|15|
|5499|Android Development Tutorial|54|1.9 MB|125|
|5501|Arch Linux Environment Setup How-To|68|1.5 MB|106|
|5503|Art Of Java Web Development|627|4.6 MB|191|
|5505|Asp.Net 2.0 Visual Web Developer 2005 Express Edition Starter Kit|314|12.7 MB|62|
|5507|Beginners Guide To C# And The .Net Micro Framework|58|676.4 KB|95|
|5509|Beginning C++ Through Game Programming|433|3.6 MB|574|
|5511|Beginning Css Web Development From Novice To Professional|446|18.0 MB|174|
|5515|Beginning Iphone Sdk Programming With Objective C|549|45.8 MB|47|
|5517|Beginning Jsp Jsf And Tomcat Web Development|472|5.3 MB|66|
|5519|Beginning Linux Programming 4th Edition|819|4.4 MB|163|
|5521|Beginning Objective C|391|4.5 MB|89|
|5523|Beginning PHP And  MySQL Third Edition|1080|13.2 MB|310|
|5525|Beginning PHP And MySQL Second Edition|1080|13.2 MB|102|
|5527|Beginning PHP5 And MySQL 5 2nd Edition|953|17.4 MB|59|
|5529|Beginning PHP6 Apache MySQL Web Development|838|8.4 MB|231|
|5531|Beginning Programming With Python For Dummies|411|10.5 MB|362|
|5535|Beginning Red Hat Linux 9|458|4.8 MB|87|
|5537|Beginning Visual C++ 2010|1276|31.3 MB|88|
|5539|Bioinformatics Programming Using Python|524|4.9 MB|160|
|5541|Black Hat Python|195|3.1 MB|280|
|5543|Black Hat SEO - Leeching From Authority Sites Secrets To Fast Rankings And Big Money|19|673.6 KB|238|
|5545|Building Probabilistic Graphical Models With Python|173|2.0 MB|140|
|5547|Building The Realtime User Experience|321|6.1 MB|24|
|5549|Business And Legal Forms For Graphic Designers|54|325.1 KB|48|
|5551|C Language Tutorial|124|296.2 KB|179|
|5553|C Programming|285|1.6 MB|189|
|5555|C# Programming Tutorial Lesson 1 - Introduction To Programming|21|962.2 KB|57|
|5557|Clr Via C# 4th Edition|813|5.2 MB|380|
|5559|Cocoa And Objective C Up And Running|417|6.2 MB|13|
|5561|Computer Networking|889|7.5 MB|196|
|5563|C++ 2013 For C# Developers|380|3.5 MB|197|
|5565|C++ And Object Oriented Numeric Computing For Scientists And Engineers|334|1.2 MB|145|
|5567|C++ Essentials|311|516.6 KB|59|
|5569|C++ FAQs 2nd Edition|453|1.1 MB|101|
|5571|C++ For Statisticians With A Focus On Interfacing From R And R Packages|60|250.2 KB|40|
|5575|C++ Gui Programming With Qt 4|555|6.2 MB|114|
|5577|C++ How To Program 8th Edition|1302|17.8 MB|298|
|5579|C++ Mini Course|60|368.2 KB|63|
|5581|C++ Network Programming Volume I|302|4.8 MB|241|
|5583|C++ Pocket Reference|138|579.7 KB|241|
|5585|C++ Primer Plus 5th Edition|1225|6.4 MB|92|
|5589|C++ Programming In Easy Steps 4th Edition|193|5.8 MB|570|
|5591|C++ Programming Tutorial And Instructions For Practical Sessions|119|599.4 KB|51|
|5593|C++ Today - The Beast Is Back|74|2.4 MB|280|
|5595|Creating A Poster In Powerpoint 2010|12|959.8 KB|36|
|5597|Creating Apps In Kivy|139|5.4 MB|172|
|5599|Creating Your MySQL Database Practical Design Tips And Techniques|105|1.2 MB|152|
|5601|C# Deconstructed - How C# Works On .Net Framework|165|5.1 MB|283|
|5603|C# eBook|338|3.3 MB|133|
|5605|C# Programming By Wikibooks Contributors|71|512.3 KB|137|
|5607|C# Programming|175|1.1 MB|103|
|5609|Data Structures And Algorithm Analysis In C++ 4th Edition|654|3.4 MB|333|
|5611|Data Structures And Algorithms In Java Second Edition|770|3.4 MB|143|
|5613|Data Structures And Algorithms In Python|770|4.9 MB|297|
|5615|Data Structures And Algorithms Using C#|366|3.8 MB|365|
|5617|Database Design Manual Using MySQL For Windows|220|6.0 MB|139|
|5619|Datastructures And Algorithmsusing Visual Basic.Net|412|1.7 MB|131|
|5621|Defensive Database Programming With SQL Server|292|2.2 MB|58|
|5623|Design For Web Developers - Colour And Layout|222|8.6 MB|99|
|5625|Designing A Graphical User Interface|8|50.9 KB|67|
|5627|Designing And Implementing Linux Firewalls And Qos|285|6.3 MB|170|
|5629|Drupal 7 Social Networking|327|4.9 MB|148|
|5631|Eclipse C C++ Programming And Fortran Course|83|1.2 MB|57|
|5633|Eclipse C++ Tutorial|17|2.0 MB|78|
|5639|Effective C++ - 50 Ways To Improve Programs And Designs|443|4.5 MB|224|
|5643|Endnote X7 Word 2013|27|1.0 MB|31|
|5645|Essential Pascal 2nd Edition|94|489.2 KB|19|
|5647|Essential System Administration 3rd Edition|1178|8.3 MB|61|
|5649|Excel 2007 2010 Tips Tricks Guide|22|1.6 MB|86|
|5653|Excel 2007 Data Statistics Cookbook|85|1.5 MB|84|
|5655|Excel 2010 Advanced|168|8.0 MB|105|
|5657|Excel 2013 Basics Quick Guide|4|594.1 KB|64|
|5659|Excel 2013 Quick Start Guide|6|293.3 KB|105|
|5661|Excel Analytics And Programming|250|6.1 MB|192|
|5663|Excel For Advanced User|175|9.1 MB|352|
|5665|Expert MySQL|598|9.5 MB|148|
|5667|Fedora 10 And Red Hat Enterprise Linux Bible|1132|10.9 MB|54|
|5669|Fedora 11 And Red Hat Enterprise Linux Bible|1132|11.5 MB|90|
|5671|Flash Mx 2004 Fast And Easy Web Development|211|11.3 MB|30|
|5673|Foundations Of Centos Linux|530|8.0 MB|133|
|5675|Fundamentals Of C++ Programming|638|6.7 MB|107|
|5677|Game Architecture And Design A New Edition|960|4.4 MB|155|
|5679|Getting Started With Beaglebone|143|5.4 MB|37|
|5681|Getting Started With Pyparsing|65|507.9 KB|223|
|5683|Ggplot2 Elegant Graphics For Data Analysis|222|6.0 MB|48|
|5685|Gpu Programming Using Cuda C C++|54|1.2 MB|92|
|5687|Graphic Designe Guide Clients|257|1.8 MB|72|
|5689|Grok 1.0 Web Development|307|2.8 MB|21|
|5691|Guide To SQL Server Maintenance Plans|270|5.9 MB|59|
|5693|Hacking Exposed Linux 3rd Edition|649|6.6 MB|195|
|5695|Head First Networking|538|17.4 MB|224|
|5697|High Performance Python|370|6.1 MB|288|
|5699|History Of Graphic Design|330|15.2 MB|35|
|5701|How Linux Works 2nd Edition|338|5.1 MB|1308|
|5703|How To Become An Exceptional Dba|174|816.7 KB|28|
|5705|How To Use Microsoft Excel 2007|12|570.5 KB|73|
|5707|Icefaces 1.8 Next Generation Enterprise Web Development|292|6.2 MB|51|
|5709|Inside Business Graphic Design Catharine Fishel|289|728.9 KB|88|
|5711|Inside The SQL Server Query Optimizer|252|2.3 MB|106|
|5713|Interfacing C C++ And Python With Swig|115|189.1 KB|133|
|5715|Interior Design Visual Presentation A Guide To Graphics, Models And Presentation Techniques 2nd Edition|250|12.0 MB|99|
|5717|Internetworking With Tcp Ip Principles Protocols And Architecture|733|2.5 MB|44|
|5719|Introduction To Algorithms|90|1.3 MB|25|
|5721|Introduction To C# A Component Oriented Language|41|160.2 KB|149|
|5723|Introduction To Java Threads|52|1.3 MB|84|
|5725|Introduction To Microsoft Excel 2003|41|382.5 KB|48|
|5727|Introduction To Microsoft Word 2003|64|612.1 KB|25|
|5729|Introduction To Object Oriented Programming Using C|115|453.1 KB|26|
|5731|Introduction To Outlook 2007|34|2.0 MB|18|
|5733|Introduction To Programming In Java|191|6.1 MB|58|
|5735|Introduction To Programming With Java 3D|613|2.8 MB|65|
|5737|Introduction To Publisher 2010 Tutorial|14|1.7 MB|16|
|5739|Introduction To VB.Net Manual|327|3.0 MB|78|
|5741|Introduction To Visual Basic.Net Programming|66|4.8 MB|67|
|5743|Introduction To Visual Studio And C#|49|2.0 MB|141|
|5745|Introduction To Word|36|1.9 MB|34|
|5749|Java 2 Web Developer Certification Study Guide|532|6.4 MB|112|
|5753|Java For Python Programmers|37|257.8 KB|135|
|5755|Learn Objective C For Java Developers|506|4.1 MB|110|
|5757|Learn Objective C On The Mac For Os X And Ios 2nd Edition|371|17.1 MB|171|
|5759|Learn Raspberry Pi With Linux|273|5.5 MB|927|
|5761|Learning Cocoa With Objective C 2nd Edition|461|5.5 MB|62|
|5763|Learning Cocoa With Objective C 3rd Edition|360|4.6 MB|66|
|5765|Learning Cocoa With Objective C 4th Edition|388|7.5 MB|134|
|5767|Learning Jquery|376|6.5 MB|220|
|5769|Learning Object Oriented Programming In C# 5.0|671|5.3 MB|331|
|5771|Learning Objective C 2|407|3.0 MB|15|
|5773|Learning Objective C By Developing Iphone Games|284|7.4 MB|24|
|5775|Learning Python 4th Edition|1213|8.7 MB|277|
|5777|Learning To Program  With Visual Basic And .Net Gadgeteer|125|3.3 MB|55|
|5779|Learning Web Design - A Beginners Guide To HTML CSS And Web Graphics 3rd Edition|481|17.1 MB|371|
|5781|Linux Appliance Design|388|7.9 MB|141|
|5783|Linux Bible 2006 Edition|912|7.4 MB|77|
|5785|Linux Bible 2010 Edition|915|9.6 MB|110|
|5787|Linux Command Line And Shell Scripting Bible 2nd Edition|723|5.8 MB|81|
|5789|Linux Command Line And Shell Scripting Bible|843|9.6 MB|213|
|5791|Linux In A Nutshell 6th Edition|944|5.5 MB|177|
|5793|Linux Iptables Pocket Reference|97|1.4 MB|341|
|5795|Linux Kernel Networking|636|3.9 MB|228|
|5797|Linux Mint Essentials|324|7.7 MB|134|
|5799|Microsoft Office Advanced Word 2013|71|2.8 MB|62|
|5801|.NET Multithreading|358|10.2 MB|83|
|5803|3D Printing With Sketchup|136|3.6 MB|36|
|5808|Adoption Centric Usability Engineering|160|2.4 MB|13|
|5810|Agile Documentation A Pattern Guide For Software Projects|245|2.6 MB|104|
|5814|Arch Linux Environment Setup How To|68|1.5 MB|134|
|5816|Arquillian Testing Guide|242|1.8 MB|24|
|5818|ASP.Net 3.5 For Dummies|434|4.3 MB|61|
|5820|Big Data Data Mining And Machine Learning|289|2.8 MB|65|
|5822|Building Applications For The Mac App Store|26|2.6 MB|31|
|5824|Building Embedded Linux Systems 2nd Edition|464|4.3 MB|129|
|5828|Business Innovation For Dummies|388|4.3 MB|27|
|5830|Centos 6 Linux Server Cookbook|374|3.8 MB|169|
|5832|Cherrypy Essentials Rapid Python Web Application Development|270|3.2 MB|181|
|5834|Clojure For Machine Learning|292|3.3 MB|66|
|5836|Concurrent Programming In Mac Os X And Ios|58|776.9 KB|92|
|5838|C++ For Dummies 7th Edition Book|477|3.5 MB|3507|
|5842|Customer Analytics For Dummies|340|4.0 MB|39|
|5844|Debian 7 System Administration Best Practices|124|1.5 MB|30|
|5846|Designing Components with the C++ STL A New Approach to Programming|307|1.0 MB|193|
|5848|Essential SQL Alchemy|230|1.5 MB|43|
|5852|Foundations Of Empirical Software Engineering|437|4.4 MB|46|
|5854|Google Plus For Dummies Portable Edition|146|3.6 MB|79|
|5856|Home Computing Weekly Technology Magazine 001|48|1.4 MB|10|
|5858|Home Computing Weekly Technology Magazine 002|48|1.3 MB|9|
|5860|Home Computing Weekly Technology Magazine 003|48|1.3 MB|9|
|5862|Home Computing Weekly Technology Magazine 004|48|1.8 MB|10|
|5864|Home Computing Weekly Technology Magazine 005|48|1.8 MB|10|
|5866|Home Computing Weekly Technology Magazine 006|48|1.8 MB|9|
|5868|Home Computing Weekly Technology Magazine 007|48|1.8 MB|10|
|5870|Home Computing Weekly Technology Magazine 008|48|1.8 MB|10|
|5872|Home Computing Weekly Technology Magazine 009|48|1.7 MB|10|
|5875|Home Computing Weekly Technology Magazine 010|48|1.6 MB|10|
|5881|Home Computing Weekly Technology Magazine 011|48|1.7 MB|10|
|5886|Home Computing Weekly Technology Magazine 012|48|1.9 MB|12|
|5895|Home Computing Weekly Technology Magazine 013|48|1.8 MB|12|
|5901|Home Computing Weekly Technology Magazine 014|48|1.6 MB|12|
|5907|Home Computing Weekly Technology Magazine 015|48|1.7 MB|11|
|5912|Home Computing Weekly Technology Magazine 016|48|1.6 MB|14|
|5915|Home Computing Weekly Technology Magazine 017|48|1.8 MB|11|
|5917|Home Computing Weekly Technology Magazine 018|48|1.7 MB|11|
|5919|Home Computing Weekly Technology Magazine 019|48|1.8 MB|11|
|5921|Home Computing Weekly Technology Magazine 020|48|1.7 MB|15|
|5926|Home Computing Weekly Technology Magazine 021|48|1.2 MB|15|
|5931|Home Computing Weekly Technology Magazine 022|40|1.5 MB|13|
|5935|Home Computing Weekly Technology Magazine 023|40|1.5 MB|21|
|5940|Home Computing Weekly Technology Magazine 024|40|1.5 MB|48|
|5942|Home Computing Weekly Technology Magazine 025|48|1.6 MB|8|
|5944|Home Computing Weekly Technology Magazine 026|40|1.4 MB|8|
|5946|Home Computing Weekly Technology Magazine 027|48|1.7 MB|8|
|5948|Home Computing Weekly Technology Magazine 028|48|1.7 MB|8|
|5950|Home Computing Weekly Technology Magazine 029|56|2.0 MB|7|
|5952|Home Computing Weekly Technology Magazine 031|48|1.9 MB|8|
|5954|Home Computing Weekly Technology Magazine 032|48|1.8 MB|8|
|5956|Home Computing Weekly Technology Magazine 033|56|1.8 MB|8|
|5958|Home Computing Weekly Technology Magazine 034|48|1.6 MB|8|
|5960|Home Computing Weekly Technology Magazine 035|48|1.8 MB|8|
|5962|Home Computing Weekly Technology Magazine 043|48|1.8 MB|9|
|5964|Home Computing Weekly Technology Magazine 044|48|1.8 MB|9|
|5966|Home Computing Weekly Technology Magazine 049|56|2.0 MB|8|
|5968|Home Computing Weekly Technology Magazine 050|48|1.6 MB|8|
|5970|Home Computing Weekly Technology Magazine 051|56|2.0 MB|8|
|5972|Home Computing Weekly Technology Magazine 053|56|2.0 MB|8|
|5974|Home Computing Weekly Technology Magazine 055|56|2.0 MB|8|
|5976|Home Computing Weekly Technology Magazine 056|48|1.7 MB|8|
|5978|Home Computing Weekly Technology Magazine 059|48|1.8 MB|8|
|5980|Home Computing Weekly Technology Magazine 060|40|1.3 MB|8|
|5982|Home Computing Weekly Technology Magazine 061|48|1.7 MB|8|
|5984|Home Computing Weekly Technology Magazine 062|48|1.7 MB|8|
|5986|Home Computing Weekly Technology Magazine 063|48|1.7 MB|9|
|5988|Home Computing Weekly Technology Magazine 066|40|1.5 MB|9|
|5990|Home Computing Weekly Technology Magazine 067|40|1.5 MB|9|
|5992|Home Computing Weekly Technology Magazine 068|40|1.4 MB|9|
|5994|Home Computing Weekly Technology Magazine 069|40|1.5 MB|9|
|5996|Home Computing Weekly Technology Magazine 070|32|1.2 MB|9|
|5998|Home Computing Weekly Technology Magazine 071|32|1.1 MB|9|
|6000|Home Computing Weekly Technology Magazine 072|32|1.1 MB|9|
|6002|Home Computing Weekly Technology Magazine 073|32|1.1 MB|9|
|6004|Home Computing Weekly Technology Magazine 074|40|1.3 MB|8|
|6006|Home Computing Weekly Technology Magazine 075|32|1.1 MB|8|
|6008|Home Computing Weekly Technology Magazine 076|32|1.1 MB|8|
|6010|Home Computing Weekly Technology Magazine 077|32|1.1 MB|9|
|6012|Home Computing Weekly Technology Magazine 078|40|1.3 MB|9|
|6014|Home Computing Weekly Technology Magazine 079|32|1.1 MB|9|
|6016|Home Computing Weekly Technology Magazine 080|40|1.4 MB|9|
|6018|Home Computing Weekly Technology Magazine 082|40|1.3 MB|9|
|6020|Home Computing Weekly Technology Magazine 083|32|1.2 MB|9|
|6022|Home Computing Weekly Technology Magazine 084|32|1.1 MB|9|
|6024|Home Computing Weekly Technology Magazine 085|32|1.2 MB|8|
|6026|Home Computing Weekly Technology Magazine 086|48|1.6 MB|9|
|6028|Home Computing Weekly Technology Magazine 087|48|1.6 MB|9|
|6030|Home Computing Weekly Technology Magazine 088|48|1.6 MB|9|
|6032|Home Computing Weekly Technology Magazine 089|48|1.8 MB|9|
|6034|Home Computing Weekly Technology Magazine 090|48|1.5 MB|9|
|6036|Home Computing Weekly Technology Magazine 091|48|1.6 MB|9|
|6038|Home Computing Weekly Technology Magazine 092|48|1.6 MB|9|
|6040|Home Computing Weekly Technology Magazine 094|48|1.6 MB|13|
|6042|Home Computing Weekly Technology Magazine 095|48|1.5 MB|9|
|6044|Home Computing Weekly Technology Magazine 096|48|1.7 MB|10|
|6046|Home Computing Weekly Technology Magazine 097|48|1.6 MB|9|
|6048|Home Computing Weekly Technology Magazine 098|48|1.6 MB|9|
|6050|Home Computing Weekly Technology Magazine 099|48|1.7 MB|11|
|6052|Home Computing Weekly Technology Magazine 100|48|1.6 MB|9|
|6054|Home Computing Weekly Technology Magazine 101|48|1.6 MB|11|
|6056|Home Computing Weekly Technology Magazine 102|56|2.0 MB|9|
|6058|Home Computing Weekly Technology Magazine 103|48|1.6 MB|9|
|6060|Home Computing Weekly Technology Magazine 104|48|1.7 MB|10|
|6062|Home Computing Weekly Technology Magazine 105|48|1.7 MB|10|
|6064|Home Computing Weekly Technology Magazine 106|48|1.7 MB|9|
|6066|Home Computing Weekly Technology Magazine 107|48|1.7 MB|12|
|6068|Home Computing Weekly Technology Magazine 108|48|1.7 MB|11|
|6070|Home Computing Weekly Technology Magazine 109|48|1.7 MB|14|
|6072|Home Computing Weekly Technology Magazine 110|48|1.5 MB|10|
|6074|Home Computing Weekly Technology Magazine 111|48|1.6 MB|9|
|6076|Home Computing Weekly Technology Magazine 112|48|1.2 MB|8|
|6078|Home Computing Weekly Technology Magazine 113|48|1.6 MB|10|
|6080|Home Computing Weekly Technology Magazine 114|48|1.7 MB|10|
|6082|Home Computing Weekly Technology Magazine 115|48|1.6 MB|9|
|6084|Home Computing Weekly Technology Magazine 116|48|1.6 MB|10|
|6086|Home Computing Weekly Technology Magazine 117|48|1.7 MB|9|
|6088|Home Computing Weekly Technology Magazine 118|48|1.8 MB|10|
|6090|Home Computing Weekly Technology Magazine 119|48|1.8 MB|10|
|6092|Home Computing Weekly Technology Magazine 120|48|1.7 MB|9|
|6094|Home Computing Weekly Technology Magazine 121|48|1.7 MB|10|
|6096|Home Computing Weekly Technology Magazine 122|40|1.3 MB|10|
|6098|Home Computing Weekly Technology Magazine 123|48|1.7 MB|10|
|6100|Home Computing Weekly Technology Magazine 124|48|1.6 MB|9|
|6102|Home Computing Weekly Technology Magazine 125|40|1.3 MB|14|
|6104|Home Computing Weekly Technology Magazine 126|40|1.3 MB|18|
|6106|Home Computing Weekly Technology Magazine 127|40|1.4 MB|12|
|6108|Home Computing Weekly Technology Magazine 128|48|1.6 MB|11|
|6110|Home Computing Weekly Technology Magazine 129|40|1.3 MB|14|
|6112|Home Computing Weekly Technology Magazine 130|40|1.4 MB|13|
|6114|Home Computing Weekly Technology Magazine 131|40|1.4 MB|12|
|6116|Home Computing Weekly Technology Magazine 132|40|1.4 MB|19|
|6118|J2ee And Xml Development|298|2.0 MB|42|
|6120|Java And Xml Data Binding|200|1.2 MB|89|
|6122|Javafx For Dummies|436|4.6 MB|584|
|6124|Learning Objective C 2.0|407|2.2 MB|105|
|6126|Learning Selenium Testing Tools With Python|216|3.2 MB|263|
|6128|Linux Device Drivers 3rd Edition|638|3.4 MB|180|
|6130|Linux Kernel Development 3rd Edition|468|2.0 MB|156|
|6132|Linux Kernel In A Nutshell|200|1.7 MB|160|
|6134|Linux Network Administrators Guide 3rd Edition|364|2.6 MB|240|
|6136|Linux Networking Clearly Explained|382|1.3 MB|357|
|6138|Linux Networking Cookbook|640|2.8 MB|377|
|6140|Linux Pocket Guide 2nd Edition|228|3.1 MB|164|
|6142|Linux Shell Scripting Cookbook 2nd Edition|384|3.0 MB|246|
|6144|Linux System Administration Recipes|282|4.3 MB|211|
|6146|Linux System Administration|296|2.7 MB|206|
|6148|Linux System Programming|390|2.1 MB|97|
|6150|Linux Thin Client Networks Design And Deployment|173|3.2 MB|107|
|6152|Looking Closer 5 - Graphic Design As System|257|1.1 MB|51|
|6154|Lpi Linux Certification In A Nutshell 3rd Edition|522|4.1 MB|172|
|6156|Macbook For Dummies 3rd Edition Book|444|3.2 MB|43|
|6158|Making Games With Python And Pygame|365|3.5 MB|131|
|6160|Making Games With Pythone Pygame|365|3.7 MB|24|
|6162|Making Graphs In Microsoft Excel 2013|19|1.1 MB|19|
|6164|Managing Raid On Linux|50|869.7 KB|183|
|6166|Mastering Regular Expressions 3rd Edition|534|2.9 MB|91|
|6168|Mastering XMI Java Programming With XMI XML And UML|474|1.2 MB|118|
|6170|Microsoft C# .Net Crash Cours C#|120|1.1 MB|188|
|6172|Microsoft Excel 2010 Presenting Data Using Charts|39|3.2 MB|19|
|6174|Microsoft Excel 2013 Tutorial|25|977.2 KB|17|
|6176|Microsoft Excel Vba Programming For Dummies 2nd Edition Book|433|4.2 MB|62|
|6178|Microsoft Outlook 2007 Beginners Guide|25|1.5 MB|12|
|6180|Microsoft Outlook Advanced|69|1.8 MB|16|
|6182|Microsoft Powerpoint 2007 Tips And Tricks|6|889.8 KB|13|
|6184|Microsoft Powerpoint 2010 Advanced Presentation Techniques|45|3.9 MB|16|
|6186|Microsoft Powerpoint 2010 Product Guide|82|3.4 MB|14|
|6188|Microsoft Powerpoint 2010 Templates And Slide Masters|12|872.7 KB|14|
|6190|Microsoft Powerpoint 2013 Quick Start Guide|9|1.2 MB|22|
|6192|Microsoft Powerpoint 2013 Workshop|32|1.9 MB|20|
|6194|Microsoft Powerpoint 2013basics Of Creating A Powerpoint Presentation|6|915.2 KB|19|
|6196|Microsoft Publisher 2007|11|757.0 KB|13|
|6198|Microsoft Publisher 2010 Getting Started Guide|4|498.1 KB|14|
|6200|Microsoft Publisher 2010|11|723.6 KB|14|
|6202|Microsoft Word 2007 Essential Guide|15|609.1 KB|13|
|6204|Microsoft Word 2010 For Dummies|412|4.4 MB|25|
|6206|Microsoft Word 2010 Tutorial|18|1.0 MB|14|
|6208|Microsoft Word 2011 Basics For Mac|7|521.2 KB|21|
|6210|Microsoft Word 2013 Introduction To Styles|23|1.3 MB|22|
|6212|Microsoft Word 2013 Quick Start Guide|6|441.2 KB|18|
|6214|Microsoft Word 2013 Tabs Tables And Graphics|19|1.2 MB|59|
|6216|Microsoft Word 2013 Tips And Tricks|9|453.3 KB|29|
|6218|Mobile Marketing For Dummies|388|3.5 MB|46|
|6220|Mongodb And Python|66|4.1 MB|253|
|6222|MySQL 5.1 Plugin Development|288|2.1 MB|111|
|6224|MySQL Cookbook|1006|3.1 MB|96|
|6226|MySQL In A Nutshell|461|1.8 MB|55|
|6228|MySQL Reference Manual|1034|3.3 MB|117|
|6230|MySQL Stored Procedure Programming|638|4.6 MB|209|
|6232|MySQL Troubleshooting|264|1.6 MB|235|
|6234|Natural Language Processing With Python|504|3.6 MB|220|
|6236|Networking And Online Games|223|3.7 MB|107|
|6238|Networking Bible|31|457.9 KB|130|
|6240|Non Programmers Tutorial For Python|128|1.3 MB|93|
|6242|NoSQL For Dummies|459|3.3 MB|73|
|6244|Object Oriented Programming In C# For C And Java Programmers|485|2.9 MB|272|
|6246|Object Oriented Programming In Visual Basic .Net Module 5|86|1.4 MB|42|
|6248|Object Oriented Programming Using Java|221|1.4 MB|97|
|6250|Objective C Phrasebook 2nd Edition|348|3.3 MB|84|
|6252|Objective C Programmer Reference|375|3.3 MB|114|
|6254|Objective C Quick Syntax Reference|116|1.5 MB|133|
|6256|Open Office Calc Spreadsheet Tutorial|18|378.4 KB|12|
|6258|Opencv Computer Vision With Python|122|1.4 MB|262|
|6260|Parallel Programming With Python|122|2.1 MB|257|
|6262|PHP Oracle Web Development|392|3.5 MB|201|
|6264|Pluggable Authentication Modules|119|1.1 MB|21|
|6266|Practical C++ Programming|549|2.7 MB|170|
|6268|Practical Linux Infrastructure|304|3.9 MB|264|
|6270|Practical Programming An Introduction To Computer Science Using Python|369|4.6 MB|345|
|6272|Practical State Charts In C C++ - Quantum Programming For Embedded Systems|279|2.1 MB|108|
|6274|Pro Asp.Net For SQL Server|430|2.8 MB|208|
|6276|Pro Linux Embedded Systems|445|4.1 MB|195|
|6278|Pro Linux High Availability Clustering|154|1.9 MB|333|
|6280|Pro MySQL|751|4.4 MB|114|
|6282|Pro Python System Administration 2nd Edition Book|411|4.1 MB|272|
|6284|Pro Python|363|2.7 MB|229|
|6286|Professional C++|867|3.5 MB|273|
|6288|Professional Lamp Linux Apache MySQL And PHP5 Web Development|406|3.8 MB|424|
|6290|Professional Linux Programming|507|2.8 MB|166|
|6292|Programming Clojure|297|1.2 MB|19|
|6294|Programming In Java|258|3.4 MB|65|
|6296|Programming In Objective C 4th Edition|562|4.3 MB|84|
|6298|Programming In Objective C 6th Edition|551|4.2 MB|222|
|6300|Protecting SQL Server Data|232|2.4 MB|63|
|6302|Protecting Yourself Online For Dummies|60|1.3 MB|19|
|6304|Python 3 Web Development|336|2.8 MB|546|
|6306|Python And Aws Cookbook|74|3.5 MB|292|
|6308|Python And XML|357|1.9 MB|155|
|6310|Python Cookbook 2nd Edition Book|846|2.8 MB|234|
|6312|Python Create Modify Reuse|290|2.9 MB|130|
|6314|Python For Unix And Linux System Administration|458|2.4 MB|500|
|6316|Python In Practice|323|2.1 MB|358|
|6318|Python Network Programming Cookbook|234|1.8 MB|342|
|6320|Python Pocket Reference 4th Edition Book|210|1.3 MB|94|
|6322|Python Pocket Reference 5th Edition Book|264|3.2 MB|379|
|6324|Python Text Processing With Nltk 2 Cookbook|272|1.9 MB|104|
|6326|Python Tools For Visual Studio|122|3.5 MB|288|
|6328|Relationships Amongst Objects|30|262.4 KB|16|
|6330|Ruby Developers Guide|721|4.1 MB|27|
|6332|Sams Teach Yourself PHP MySQL And Apache All In One|645|4.3 MB|366|
|6334|Sams Teach Yourself XML In 21 Days Third Edition Book|98|729.9 KB|199|
|6336|Scipy And Numpy|66|2.3 MB|36|
|6338|Serialization In Java (Binary And XML)|11|729.9 KB|96|
|6340|Smart Home Automation With Linux|313|4.6 MB|183|
|6342|Software Defined Networking|176|1.4 MB|291|
|6344|Spring Web Flow 2 Web Development|272|2.7 MB|93|
|6346|SQL Server Backup And Restore|381|3.4 MB|83|
|6348|SQL Server Concurrency Locking Blocking And Row Versioning|181|1.3 MB|126|
|6350|SQL Server Statistics|44|1,007.4 KB|57|
|6352|SQL Server Tacklebox Essential Tools And Scripts For Dba|232|3.9 MB|67|
|6354|SQL Server Team-Based Development|349|4.1 MB|48|
|6356|SQL Server Transaction Log Management|209|1.6 MB|79|
|6358|Stripes And Java Web Development|389|2.6 MB|60|
|6360|Subdivision Methods For Geometric Design A Constructive Approach|316|3.4 MB|19|
|6362|Svg Essentials Producing Scalable Vector Graphics With XML|25|2.3 MB|79|
|6364|Teach Yourself C++ In 21 Days 5th Edition|937|3.1 MB|336|
|6366|Telling Stories A Short Path To Writing Better Software Requirements|163|1.9 MB|90|
|6368|The 2007-2012 Microsoft Outlook For Graphic Design Services In The United States|683|3.2 MB|40|
|6370|The C Book Featuring The Ansi C Standard|330|2.5 MB|330|
|6372|The Definitive Guide To Django Web Development Done Right|481|4.1 MB|60|
|6374|The Education Of A Graphic Designer Second Edition|369|1.4 MB|175|
|6376|The Graphic Design Business Book|257|1.6 MB|118|
|6378|The Linux Cookbook Tips And Techniques For Everyday Use|544|3.6 MB|98|
|6380|The Snake Game Java Case Study|35|172.5 KB|129|
|6382|Think Complexity|146|1.1 MB|25|
|6384|Think Stats|125|1.6 MB|15|
|6386|Tips And Tricks For Microsoft Powerpoint 2007|11|402.5 KB|40|
|6388|Tips And Tricks Word September 2013|29|1.3 MB|54|
|6390|Tribal SQL Extract SQL Server Storage Internals 101|20|593.6 KB|47|
|6392|Troubleshooting SQL Server A Guide For The Accidental Dba|358|2.4 MB|109|
|6394|Two Minute SQL Server Stumpers|208|466.3 KB|52|
|6396|Understanding C++ An Accelerated Introduction|63|505.6 KB|60|
|6398|Understanding The Linux Kernel 3rd Edition|944|4.3 MB|306|
|6400|Using C++ With Netbeans For Introduction To Programming With C++|8|818.1 KB|0|
|6402|Using Samba 3rd Edition|449|3.4 MB|125|
|6404|VB.Net Tutorial For Beginners|243|3.7 MB|65|
|6406|Virtualization For Dummies|386|4.5 MB|32|
|6408|Visual Basic.Net For Xamarin Using Portable Class Libraries|15|1.1 MB|44|
|6410|Visual Basic Books|260|1.5 MB|1|
|6412|Visual C++ 2010 Tutorial|16|2.6 MB|73|
|6414|Visual C++ 2012 Tutorial|10|597.8 KB|77|
|6416|Web Development With Java|300|1.9 MB|286|
|6420|Working With Video In Powerpoint 2013|12|1.6 MB|44|
|6422|XML For Dummies|386|3.4 MB|99|
|6424|XML Pocket Reference 2nd Edition Book|70|423.4 KB|74|
|6426|XML Publishing With Indesign CS|110|1.8 MB|25|
|6438|.Net Framework 4.5 Expert Programming Cookbook|276|3.6 MB|120|
|6440|.NET Framework Essentials, 2nd Edition|257|2.7 MB|117|
|6442|.NET IL Assembler|476|2.9 MB|118|
|6444|3D Animation for the Raw Beginner Using Maya|472|12.2 MB|116|
|6446|A Concise Windows 8 Guide- For Homes and Corporates|526|8.9 MB|27|
|6448|ABAP Cookbook|553|8.4 MB|157|
|6450|ABAP to the Future|731|11.1 MB|32|
|6452|Active Directory, 5th Edition|738|10.6 MB|153|
|6454|Adobe Dreamweaver CC For Dummies|419|12.1 MB|246|
|6456|Adobe Dreamweaver CS6 Bible|1225|14.1 MB|293|
|6458|Adobe Dreamweaver CS6 Classroom in a Book|448|12.4 MB|229|
|6460|Adobe Dreamweaver CS6 Digital Classroom|498|11.1 MB|187|
|6462|Adobe Dreamweaver CS6 on Demand|609|13.8 MB|166|
|6464|Adobe Flash Professional CS5 on Demand|577|12.0 MB|80|
|6466|Adobe Premiere Pro CS6 Classroom in a Book|501|16.7 MB|109|
|6468|AdvAnce PrAise for Perl One Liners|168|5.3 MB|24|
|6470|Advances in Neural Networks Computational and Theoretical Issues|392|9.7 MB|30|
|6472|Agent-Based Modeling and Simulation with Swarm|316|11.8 MB|11|
|6476|Android Developer Tools Essentials|248|9.7 MB|134|
|6478|Android for Work|309|6.5 MB|155|
|6482|Android Native Development Kit Cookbook|346|4.1 MB|186|
|6484|Android on x86|375|4.9 MB|81|
|6486|Android Programming for Beginners|698|5.9 MB|351|
|6488|Android Recipes, 3rd Edition|760|3.3 MB|142|
|6490|Android Security- Attacks and Defenses|272|3.7 MB|214|
|6492|AOP in .NET - Practical Aspect-Oriented Programming|298|3.1 MB|91|
|6496|App Inventor|385|5.9 MB|18|
|6498|Applied XML Programming for Microsoft .NET|536|6.0 MB|42|
|6500|Arista Warrior|421|4.8 MB|139|
|6502|Authorizations in SAP|351|14.5 MB|22|
|6504|Automation through Chef Opscode|255|10.1 MB|59|
|6506|Beginning Android 3|581|8.6 MB|89|
|6508|Beginning Android 4|575|8.0 MB|191|
|6510|Beginning Android Application Development|450|5.8 MB|208|
|6514|Beginning Perl for Bioinformatics|394|1.0 MB|37|
|6516|Beginning Perl|748|3.5 MB|69|
|6518|Beginning Scala|246|1.5 MB|269|
|6520|Beginning SharePoint 2013|676|17.3 MB|108|
|6522|Beginning WF Windows Workflow in .NET 4.0|471|3.1 MB|40|
|6524|Beginning WF|471|3.1 MB|11|
|6526|Beginning Windows 8 Data Development|245|4.5 MB|19|
|6528|Beginning Windows Phone 7 Development, 2nd Edition|502|16.7 MB|17|
|6530|Beginning Windows Phone App Development|538|13.5 MB|18|
|6532|BMC Control-M 7|534|9.3 MB|12|
|6534|Building a Windows IT Infrastructure in the Cloud|186|4.8 MB|52|
|6538|Building Windows 8.1 Apps From The Ground Up|377|17.6 MB|34|
|6540|Cartoon Character Animation with Maya|292|8.5 MB|254|
|6542|Citrix XenDesktop 7 Cookbook|410|10.8 MB|41|
|6544|Code-First Development with Entity Framework|174|1.4 MB|144|
|6546|Computer Vision for X-Ray Testing|362|17.6 MB|42|
|6548|Continuous Integration in .NET|331|9.3 MB|143|
|6550|C# 6.0 and the .NET 5 Framework, 7th edition|1837|15.2 MB|797|
|6552|Data Center Handbook|717|14.4 MB|122|
|6554|Data Mining The Textbook|746|10.8 MB|74|
|6556|Designing for Emotion|112|3.0 MB|108|
|6558|Designing the Search Experience|320|15.1 MB|92|
|6560|Developer-s Guide to Collections in Microsoft .NET|648|6.0 MB|66|
|6562|Developing Android on Android|220|2.8 MB|322|
|6564|Developing for Apple TV using tvOS and Swift|134|5.7 MB|123|
|6566|Digital Audio Editing Fundamentals|151|12.6 MB|119|
|6568|Digital Security- Cyber Terror and Cyber Security|121|12.0 MB|1461|
|6570|Do more with SOA Integration Best of Packt|702|8.6 MB|31|
|6572|Dreamweaver 8 For Dummies|451|4.7 MB|58|
|6574|Dreamweaver CC Digital Classroom|514|15.5 MB|166|
|6576|Dreamweaver CC The Missing Manual, 2nd Edition|1029|16.1 MB|242|
|6578|Dreamweaver CS3 The Missing Manual|1021|10.4 MB|43|
|6580|Dreamweaver CS6 The Missing Manual|1034|13.9 MB|115|
|6582|Dreamweaver MX 2004 Bible|1227|10.5 MB|38|
|6584|Dreamweaver Mx Bible|1226|10.6 MB|59|
|6588|Effective Akka|72|1.5 MB|46|
|6590|Enterprise iPhone and iPad Administrators Guide|393|16.6 MB|59|
|6592|Entity Framework 4 in Action|578|8.9 MB|73|
|6594|Essential Algorithms|758|4.8 MB|51|
|6596|Essential Windows Phone 7.5|513|6.1 MB|17|
|6598|Evolutionary Optimization Algorithms|776|10.4 MB|30|
|6602|Expert .NET Micro Framework|448|6.6 MB|72|
|6604|Extending SSIS with .NET Scripting|481|16.1 MB|150|
|6606|Fsharp for C# Developers|640|5.7 MB|165|
|6608|Functional Programming in Scala|304|2.9 MB|202|
|6610|Functional Programming Patterns in Scala and Clojure|253|5.3 MB|247|
|6612|Future-Proof Web Design|402|16.9 MB|113|
|6614|Game Development with Swift|224|3.4 MB|147|
|6616|Games, Diversions - Perl Culture|1252|4.3 MB|41|
|6618|Getting Started with .NET Gadgeteer|87|4.3 MB|50|
|6620|Getting Started With Citrix Xenapp 7.6|460|9.1 MB|809|
|6622|Getting Started with Knockoutdotjs for .NET Developers|188|1.5 MB|41|
|6624|Getting Started with PowerShell|180|7.2 MB|341|
|6626|Getting Started with Windows VDI|303|7.4 MB|76|
|6628|Git Version Control Cookbook|340|3.8 MB|206|
|6630|Guide To Troubleshooting Windows XP - Its Never Done That Before|283|4.5 MB|37|
|6632|Handbook of Metadata, Semantics and Ontologies|579|6.2 MB|63|
|6636|Heterogeneous Computing with OpenCL, 2nd Edition|299|6.7 MB|176|
|6638|Human-Computer Interface Technologies for the Motor Impaired|212|13.1 MB|31|
|6640|Illustrated WPF|530|8.5 MB|68|
|6642|Image Encryption- A Communication Perspective|406|7.4 MB|81|
|6644|Innovative Software Development in GIS|336|5.6 MB|42|
|6646|Inside Microsoft Dynamics AX 2012|784|18.5 MB|35|
|6648|Intermediate Perl, 2nd Edition|396|3.7 MB|134|
|6650|Introducing Microsoft System Center 2012 R2|180|7.4 MB|80|
|6652|Introducing Windows Server 2012 RTM Edition|256|10.4 MB|58|
|6654|Introduction to Biometrics|328|10.9 MB|21|
|6656|iOS 8 SDK Development, 2nd Edition|288|5.6 MB|55|
|6658|iOS 9 Swift Programming Cookbook|713|7.6 MB|612|
|6660|iOS Swift Game Development Cookbook Second Edition|405|4.0 MB|226|
|6662|JIRA Essentials - Third Edition|390|10.1 MB|71|
|6664|Learn PowerShell Toolmaking in a Month of Lunches|311|7.5 MB|347|
|6666|Learn Swift On The Mac|254|4.5 MB|117|
|6668|Learn Windows IIS in a Month of Lunches|369|11.0 MB|139|
|6670|Learn Windows PowerShell 3 in a Month of Lunches, 2nd Edition|367|6.0 MB|810|
|6674|Learning Android, 2nd Edition|288|6.0 MB|204|
|6676|Learning .NET High performance Programming|305|12.2 MB|163|
|6680|Learning Perl, 6th Edition|390|3.6 MB|208|
|6682|Learning Play Framework 2|290|8.2 MB|80|
|6684|Learning Scala|255|2.6 MB|451|
|6686|Learning Swift 2 Programming, 2nd Edition|882|9.2 MB|122|
|6688|Learning Swift|266|2.9 MB|77|
|6690|Lift Cookbook|253|2.3 MB|42|
|6692|Lift in Action The simply functional web framework for Scala|426|5.7 MB|139|
|6694|Lift in Action|426|5.7 MB|8|
|6696|Lift Web Applications How-to|96|1.1 MB|37|
|6698|LINQ in Action|572|6.2 MB|58|
|6702|Machine Learning Projects for .NET Developers|290|6.0 MB|561|
|6704|Mastering Active Directory for Windows Server 2008|771|10.2 MB|85|
|6706|Mastering Algorithms with Perl|739|6.0 MB|66|
|6708|Mastering Eclipse Plug-in Development|362|5.3 MB|26|
|6710|Mastering Entity Framework|304|3.2 MB|184|
|6712|Mastering Microsoft Azure Infrastructure Services|385|17.3 MB|1314|
|6714|Mastering Nginx|322|2.4 MB|80|
|6716|Mastering Ninject for Dependency Injection|142|952.7 KB|189|
|6718|Mastering Perl, 2nd Edition|397|4.1 MB|185|
|6720|Mastering Swift 2 - Swift programming|408|5.4 MB|135|
|6722|Mastering Swift Swift programming language|358|3.5 MB|77|
|6724|Metaprogramming in .NET|360|7.6 MB|134|
|6726|Microsoft .NET - Architecting Applications for the Enterprise, 2nd Edition|417|5.6 MB|1715|
|6728|Microsoft .NET Framework 4.5 Quickstart Cookbook|226|4.2 MB|54|
|6730|Microsoft ADO.NET 4 Step by Step|441|6.7 MB|241|
|6732|Microsoft ADO.NET Entity Framework Step by Step|448|9.0 MB|78|
|6734|Microsoft Application Virtualization Advanced Guide|474|10.9 MB|62|
|6736|Microsoft Azure Development Cookbook Second Edition|422|3.5 MB|421|
|6738|Microsoft Azure SQL Database Step by Step|401|16.8 MB|583|
|6740|Microsoft Data Protection Manager 2010|360|7.9 MB|27|
|6742|Microsoft Virtualization Secrets|554|18.4 MB|64|
|6744|Microsoft Windows 7 Administration Instant Reference|626|9.3 MB|100|
|6746|Microsoft Windows Registry Guide, 2nd Edition|577|4.2 MB|260|
|6748|Microsoft Windows Scripting Self-Paced Learning Guide|386|2.2 MB|178|
|6750|Microsoft Windows Scripting with WMI|400|3.7 MB|145|
|6752|Microsoft Windows Server 2003 Administrators Companion, 2nd Edition|1437|12.9 MB|49|
|6754|Microsoft Windows XP Networking and Security Inside Out|700|9.2 MB|68|
|6756|Microsoft Windows XP Professional, 3rd Edition|1503|10.6 MB|45|
|6760|Migrating to Swift from Web Development|248|7.1 MB|133|
|6762|Migrating to Windows Phone|263|8.3 MB|20|
|6764|Migration from Windows Server 2008 and 2008 R2 to 2012 How-to|84|3.0 MB|50|
|6766|Mobile Clouds Exploiting Distributed Resources In Wireless, Mobile And Social Networks|222|4.2 MB|50|
|6768|Modeling, Simulation And Visual Analysis Of Crowds|414|15.8 MB|59|
|6770|More iPhone Development with Swift|480|8.0 MB|138|
|6772|NET 2.0 Interoperability Recipes|631|1.7 MB|45|
|6774|Networking for VMware Administrators|369|17.9 MB|250|
|6776|Object-Oriented Software Engineering|578|8.6 MB|245|
|6778|OData Programming Cookbook for .NET Developers|376|5.8 MB|95|
|6780|OpenCL in Action|458|2.9 MB|172|
|6782|OpenCL Parallel Programming Development Cookbook|303|2.5 MB|143|
|6784|OpenCL Programming by Example|304|3.5 MB|247|
|6786|OpenCL Programming Guide|648|4.6 MB|153|
|6788|OpenGL ES 2 for Android|330|4.1 MB|178|
|6790|OpenStack Object Storage Swift Essentials|174|3.1 MB|202|
|6792|Optimizing and Accessing Information Technology|253|16.7 MB|18|
|6794|Perl - LWP|343|1.4 MB|24|
|6796|Perl and LWP|343|1.4 MB|28|
|6798|Perl and XML|158|844.2 KB|65|
|6800|Perl One-Liners|168|5.3 MB|122|
|6802|Perl Pocket Reference, 5th Edition|101|1.3 MB|71|
|6804|PerlTk Pocket Reference|60|187.6 KB|30|
|6806|Physics for Flash Games, Animation, and Simulations|547|7.5 MB|93|
|6808|Play for Scala|330|3.3 MB|194|
|6810|PowerPivot for Business Intelligence Using Excel and SharePoint|299|16.8 MB|253|
|6812|Practical Code Generation in .NET|529|4.1 MB|130|
|6814|Practical Robot Design- Game Playing Robots|406|14.7 MB|184|
|6816|Pro .NET 2.0 XML Experts Voice in .NET|525|14.2 MB|41|
|6818|Pro .NET Best Practices|365|4.8 MB|251|
|6820|Pro Android Web Apps|382|12.9 MB|383|
|6822|Pro Asynchronous Programming with .NET|336|7.1 MB|482|
|6824|Pro Design Patterns in Swift|568|5.7 MB|253|
|6826|Pro DLR in .NET 4|329|2.9 MB|22|
|6828|Pro Dynamic .NET 4.0 Applications|265|2.7 MB|122|
|6830|Pro Freeware and Open Source Solutions for Business|265|13.7 MB|87|
|6832|Pro HTML5 with Visual Studio 2015|435|9.2 MB|395|
|6834|Pro LINQ Language Integrated Query in VB 2008|746|3.2 MB|18|
|6836|Pro LINQ|746|3.2 MB|12|
|6838|Pro Microsoft HDInsight|258|9.2 MB|40|
|6840|Pro Perl Debugging|277|2.2 MB|90|
|6842|Pro Perl|1047|4.2 MB|96|
|6844|Pro PowerShell for Database Developers|419|7.2 MB|203|
|6846|Pro Scalable .NET 2.0 Application Designs|537|8.1 MB|60|
|6848|Pro WF 4.5|638|9.9 MB|116|
|6850|Pro Windows Phone 7 Development|658|15.2 MB|18|
|6852|Pro Windows Phone App Development, 3rd Edition|551|14.4 MB|32|
|6854|Pro WPF 4.5 in C# 4th Edition|1095|13.0 MB|762|
|6856|Processing- A Programming Handbook for Visual Designers and Artists, 2 edition|663|15.2 MB|79|
|6858|Professional Apache Tomcat 6|664|17.9 MB|90|
|6860|Professional Crystal Reports for Visual Studio .NET, 2nd Edition|386|15.5 MB|140|
|6862|Professional IIS 7|843|11.1 MB|65|
|6866|Professional Swift|391|5.0 MB|195|
|6873|Professional Visual Basic 2012 and .NET 4.5 Programming|916|14.2 MB|231|
|6875|Professional WPF Programming|482|6.5 MB|44|
|6877|Programming Elastic MapReduce|173|3.6 MB|42|
|6879|Programming Entity Framework Code First|192|5.9 MB|102|
|6881|Programming Entity Framework, 2nd Edition|914|8.4 MB|267|
|6883|Programming F#|408|2.2 MB|121|
|6885|Programming Microsoft Clouds|602|14.6 MB|73|
|6888|Programming Microsoft LINQ in Microsoft .NET Framework 4|705|6.4 MB|249|
|6890|Programming Perl, 4th Edition|1176|7.9 MB|152|
|6893|Programming Scala, 2nd Edition|579|3.7 MB|435|
|6895|Programming Scala|226|1.3 MB|160|
|6897|Programming Windows Phone 7|430|4.4 MB|21|
|6899|Programming Windows, 5th Edition|1122|2.8 MB|61|
|6901|Sams Teach Yourself Dreamweaver CS5 in 24 Hours|495|11.5 MB|179|
|6904|Scala Cookbook|722|5.2 MB|865|
|6906|Scala for Java Developers|282|3.9 MB|462|
|6908|Scala in Action|418|4.1 MB|447|
|6910|Scala in Depth|306|3.0 MB|407|
|6912|SharePoint 2013 Branding and User Interface Design|432|17.4 MB|153|
|6914|SharePoint 2013 Users Guide, 4th Edition|524|12.2 MB|261|
|6916|Simply Windows 7|226|7.5 MB|30|
|6918|Source SDK Game Development Essentials|294|9.3 MB|74|
|6920|Swift 2 For Absolute Beginners, 2nd Edition|348|12.6 MB|223|
|6922|Swift by Example|285|5.0 MB|163|
|6924|Swift Cookbook|705|8.0 MB|94|
|6926|Swift Development with Cocoa|472|8.0 MB|114|
|6928|Swift Essentials|228|5.0 MB|142|
|6930|Swift for Absolute Beginners|293|10.2 MB|133|
|6932|Swift for Beginners- Develop and Design|487|10.9 MB|336|
|6934|Swift Game Programming for Absolute Beginners|353|3.7 MB|311|
|6936|Swift High Performance|351|2.3 MB|294|
|6938|Swift OS X Programming for Absolute Beginners|557|13.2 MB|200|
|6940|Swift Pocket Reference|185|1.4 MB|111|
|6942|Swift Quick Syntax Reference|158|931.9 KB|99|
|6944|Swift Recipes A Problem Solution Approach|331|3.3 MB|121|
|6946|Swift Recipes|331|3.3 MB|81|
|6948|Swift|501|4.5 MB|1|
|6950|Terrible Old Games You have Probably Never Heard Of|274|14.9 MB|424|
|6952|Testing in Scala|165|6.1 MB|264|
|6954|The Master Algorithm|353|14.2 MB|3823|
|6956|Thinking in LINQ|259|7.8 MB|113|
|6958|TI-Nspire For Dummies, 2nd Edition|387|11.3 MB|436|
|6960|TouchDevelop, 3rd Edition|271|3.4 MB|16|
|6962|Training Guide Configuring Windows 8|617|10.6 MB|42|
|6964|Training Guide Installing and Configuring Windows Server 2012|640|9.9 MB|76|
|6966|Transitioning to Swift|228|1.9 MB|96|
|6968|Visual Studio 2012 and .NET 4.5 Expert Development Cookbook|380|4.8 MB|97|
|6970|Visual Studio 2013 Cookbook|333|6.1 MB|131|
|6972|VMware ESXi Cookbook|334|10.0 MB|41|
|6974|VMware Horizon View Essentials|421|12.3 MB|44|
|6976|VMware vRealize Operations Performance and Capacity Management|276|11.4 MB|60|
|6978|Web Hosting For Dummies|362|16.6 MB|206|
|6980|Welcome to Swift|501|4.5 MB|128|
|6982|Windows 10 For Seniors For Dummies|339|11.7 MB|63|
|6984|Windows 10 Revealed|115|6.2 MB|119|
|6986|Windows 2000 Commands Pocket Reference|122|612.9 KB|30|
|6988|Windows 7 Up and Running|203|10.0 MB|41|
|6990|Windows 8 Administration Pocket Consultant|672|12.7 MB|31|
|6992|Windows Communication Foundation 4 Step by Step|737|9.5 MB|42|
|6994|Windows File System Troubleshooting|165|9.3 MB|105|
|6996|Windows Phone 7 Developer Guide|337|5.5 MB|18|
|6998|Windows Phone 7 Development Internals|837|18.7 MB|19|
|7000|Windows Phone 7 in Action|481|14.7 MB|17|
|7002|Windows Phone 7 Recipes|365|7.5 MB|18|
|7004|Windows Phone 7.5 Application Development with F-|138|4.5 MB|16|
|7006|Windows Phone 8 Application Development Essentials|118|2.1 MB|21|
|7008|Windows Phone 8 Development Internals|229|6.5 MB|21|
|7010|Windows Phone 8 Game Development|499|5.3 MB|53|
|7012|Windows Phone 8 in Action|497|7.2 MB|23|
|7014|Windows Phone 8 Recipes|417|8.7 MB|19|
|7016|Windows Phone Recipes, 2nd Edition|486|7.3 MB|18|
|7018|Windows Registry Troubleshooting|124|5.9 MB|131|
|7020|Windows Server 2003 Networking Recipes|438|3.9 MB|91|
|7022|Windows Server 2012 Automation with PowerShell Cookbook|372|6.4 MB|369|
|7024|Windows Server 2012 Hyper-V|410|8.4 MB|89|
|7026|Windows Server 2012 Pocket Consultant|718|8.1 MB|94|
|7028|Windows Server 2012 Unified Remote Access Planning and Deployment|328|8.0 MB|65|
|7030|Windows Server 2012 Up and Running|258|8.4 MB|83|
|7032|Windows Vista Annoyances|666|6.7 MB|20|
|7034|Working with NHibernate 3.0|228|6.9 MB|51|
|7036|Zabbix 1.8 Network Monitoring|428|7.9 MB|114|
|7038|Adobe Acrobat 6 Pdf For Dummies|409|4.9 MB|59|
|7042|A Handbook Of Software And Systems Engineering|346|9.0 MB|95|
|7044|Adobe Creative Suite 2 All In One Desk Reference For Dummies|769|13.0 MB|64|
|7046|Adobe Edge Animate CC For Dummies|387|13.2 MB|145|
|7048|Adobe Flash 11 Stage 3D Game Programming|412|4.9 MB|123|
|7050|Adobe Flash Professional CS5 Bible|883|15.7 MB|129|
|7052|Android Tablets For Dummies 2nd Edition Book|355|10.7 MB|368|
|7054|Android Tablets For Dummies|320|15.1 MB|213|
|7056|Autocad 2005 For Dummies|435|8.6 MB|28|
|7058|Autocad 2007 For Dummies|435|8.3 MB|37|
|7060|Autocad 2011 For Dummies|533|10.9 MB|76|
|7064|Bea Weblogic Server 8 For Dummies|385|7.4 MB|13|
|7066|Beginning ArcGIS for Desktop Development using .NET|532|19.3 MB|140|
|7068|Beginning Mac Programming|430|5.6 MB|43|
|7070|Beginning Python Visualization 2nd Edition Book|405|6.3 MB|288|
|7072|Beginning XML With Dom And Ajax|455|8.8 MB|212|
|7074|Big Data Analytics Using Splunk|362|12.2 MB|80|
|7076|Blackberry Application Development For Dummies|412|5.2 MB|8|
|7078|Blogging For Dummies 4th Edition Book|411|18.5 MB|87|
|7080|Building A Web Site For Dummies 4th Edition|365|9.1 MB|100|
|7082|Building Mapping Applications With Qgis|264|5.7 MB|56|
|7084|Building Oracle XML Applications|883|4.9 MB|53|
|7086|Calculus For Dummies 2nd Edition Book|387|5.4 MB|566|
|7088|Calculus Practice Problems For Dummies|626|8.3 MB|23|
|7090|C++ For Dummies 5th Edition Book|435|8.2 MB|297|
|7092|Creating Web Pages All In One For Dummies 4th Edition Book|652|15.1 MB|102|
|7094|Creating Web Pages For Dummies 8th Edition Book|411|6.8 MB|61|
|7096|Creating Web Pages For Dummies 9th Edition Book|340|8.5 MB|166|
|7098|C# 2010 All In One For Dummies|867|10.0 MB|374|
|7100|Data Mining For Dummies|411|9.7 MB|172|
|7102|.Net Nuke For Dummies|411|6.0 MB|83|
|7104|Droid 2 For Dummies|388|7.3 MB|12|
|7106|Electronics For Dummies|387|7.7 MB|50|
|7108|Facebook Marketing For Dummies 5th Edition Book|340|9.4 MB|314|
|7110|Fifty Years of Fuzzy Logic and its Applications Studies in Fuzziness and Soft Computing|679|19.3 MB|106|
|7112|Game Maker Studio For Dummies|356|10.3 MB|248|
|7114|Google Search And Rescue For Dummies|410|10.1 MB|113|
|7116|Google Sites And Chrome For Dummies|460|12.9 MB|76|
|7118|HTML 4 For Dummies 5th Edition Book|435|6.8 MB|50|
|7120|HTML CSS And Javascript Mobile Development For Dummies|435|13.2 MB|289|
|7122|HTML XHTML And CSS All In One Desk Reference For Dummies|962|13.9 MB|154|
|7124|HTML5 Programming With Javascript For Dummies|411|8.3 MB|1387|
|7126|iMac For Dummies 6th Edition Book|435|11.0 MB|26|
|7128|iMac For Dummies 8th Edition Book|435|12.3 MB|53|
|7130|Infographics For Dummies|323|8.9 MB|27|
|7132|Io Programmo Magzine 95|100|8.3 MB|23|
|7134|iPAD For Dummies 7th Edition Book|388|8.2 MB|72|
|7136|iPAQ For Dummies|387|5.9 MB|10|
|7138|iPhone And iPAD Game Development For Dummies|508|5.2 MB|107|
|7141|iPhone Photography And Video For Dummies|260|10.0 MB|64|
|7144|Jquery For Dummies|364|14.4 MB|309|
|7146|Lecture Notes In Computer Science Software Engineering|264|7.1 MB|69|
|7148|Linux All In One For Dummies 4th Edition Book|652|9.2 MB|93|
|7150|Linux All In One For Dummies 5th Edition Book|579|10.5 MB|420|
|7152|Linux Firewalls|338|6.0 MB|270|
|7154|Linux Mint System Administrators|147|5.2 MB|189|
|7156|Linux Recipes For Oracle Dbas|530|7.6 MB|211|
|7159|Linux System Programming 2nd Edition|456|5.4 MB|390|
|7161|Logic Pro X For Dummies|388|14.9 MB|20|
|7163|Mac Application Development By Example|318|5.8 MB|60|
|7165|Mac Application Development For Dummies|419|6.2 MB|51|
|7167|Mac Book For Dummies|387|7.2 MB|50|
|7170|Machine Learning In Action|382|5.5 MB|63|
|7172|Macs All In One Desk Reference For Dummies|819|16.9 MB|74|
|7174|Macs For Seniors For Dummies 2nd Edition Book|387|15.1 MB|42|
|7176|Mastering SQL Server Profiler|307|9.0 MB|69|
|7178|Microsoft Access 2010 For Dummies|470|13.2 MB|31|
|7180|Microsoft Access 2013 For Dummies|459|16.8 MB|40|
|7182|Microsoft Business Intelligence For Dummies|435|7.5 MB|102|
|7186|Microsoft Excel 2013 All In One For Dummies|795|19.3 MB|70|
|7188|Microsoft Excel Data Analysis For Dummies 2nd Edition Book|363|14.6 MB|77|
|7190|Microsoft Excel Formulas And Functions For Dummies 2nd Edition Book|390|6.2 MB|69|
|7192|Microsoft Office 2013 All In One For Dummies|819|16.6 MB|58|
|7194|Microsoft Office Home And Student 2010 All In One For Dummies|676|8.4 MB|19|
|7196|Microsoft Outlook 2010 All In One For Dummies|940|18.2 MB|25|
|7198|Microsoft Powerpoint 2003 Just The Steps For Dummies|219|7.0 MB|12|
|7200|Microsoft Powerpoint 2007|156|4.9 MB|14|
|7202|Microsoft Powerpoint 2013 For Dummies|355|11.5 MB|35|
|7204|Microsoft Powerpoint 2013|76|5.9 MB|15|
|7206|Microsoft Windows Intune 2.0 Quickstart Administration|312|19.0 MB|62|
|7208|Microsoft Windows Xp Networking Inside Out|700|10.4 MB|115|
|7210|Microsoft Word 2010|266|7.9 MB|56|
|7212|Modx Web Development|276|5.8 MB|47|
|7214|MySQL Admin Cookbook|372|10.1 MB|228|
|7216|MySQL Administrator Bible|891|16.1 MB|237|
|7218|MySQL And mSQL|775|5.4 MB|90|
|7220|Networking For Dummies|435|10.8 MB|490|
|7222|Object Oriented Programming In C++ Third Edition|988|5.5 MB|204|
|7224|Objective C For Absolute Beginners 2nd Edition|334|8.8 MB|256|
|7226|Objective C Fundamentals|368|5.6 MB|196|
|7228|Opensuse Linux Unleashed|733|11.9 MB|144|
|7230|Oracle 11g For Dummies|412|4.7 MB|302|
|7232|Performance Tuning Using SQL Server Dynamic Management Views|326|6.0 MB|67|
|7234|PHP Programming With MySQL Second Edition|715|9.1 MB|828|
|7236|Practical Data Science Cookbook|396|5.0 MB|197|
|7238|Practical Rails Social Networking Sites|446|7.2 MB|140|
|7240|Pro Android 2|736|9.3 MB|507|
|7242|Pro Apache XML|502|5.8 MB|113|
|7244|Pro Data Backup and Recovery|285|19.4 MB|38|
|7246|Pro Objective C|464|9.3 MB|236|
|7248|Pro Oracle Database 11g Rac On Linux 2nd Edition|830|9.9 MB|237|
|7250|Pro XML Development With Java Technology|470|11.0 MB|178|
|7252|Professional SQL Server 2005 XML|549|6.2 MB|61|
|7254|Programming In Python3 2nd Edition|636|6.8 MB|184|
|7256|Project Management For Dummies 3rd Edition Book|388|5.5 MB|47|
|7258|Python Programming For Arduino|576|8.1 MB|1365|
|7260|Quicken 2009 For Dummies|386|8.4 MB|9|
|7262|Real World Instrumentation With Python|621|7.5 MB|373|
|7264|Red Hat Linux Networking And System Administration|1029|10.2 MB|795|
|7266|Running Linux 5th Edition|974|9.4 MB|300|
|7268|Samsung Galaxy S5 For Dummies|355|12.7 MB|42|
|7270|Seam 2.X Web Development|300|7.5 MB|46|
|7272|Search Engine Optimization For Dummies 5th Edition Book|459|10.8 MB|801|
|7274|Sharepoint 2010 All In One For Dummies|916|9.3 MB|239|
|7276|Sharepoint 2013 For Dummies|387|10.1 MB|694|
|7278|Shell Scripting - Expert Recipes For Linux Bash And More|603|10.0 MB|714|
|7280|Simulation Technologies In Networking And Communications|632|13.4 MB|453|
|7282|Software Engineering And Testing|529|9.6 MB|138|
|7284|SQL All In One For Dummies 2nd Edition Book|748|9.4 MB|437|
|7286|SQL Server Execution Plans Second Edition|322|7.3 MB|80|
|7288|SQL Server Hardware|318|4.8 MB|56|
|7290|Starting Out With C++ From Control Structures Through Objects 8th Edition|1269|6.9 MB|11643|
|7292|Statistical Analysis With Excel For Dummies 2nd Edition Book|507|13.4 MB|382|
|7294|Surface For Dummies 2nd Edition Book|339|10.9 MB|16|
|7296|Swift For Dummies|387|18.9 MB|348|
|7298|Systems Graphics Breakthroughs In Drawing Production And Project Management For Architects, Designers And Engineers|268|12.0 MB|54|
|7300|Taming Apache Open Office Version 3.4|316|7.0 MB|30|
|7304|The Art Of Memory Forensics - Detecting Malware And Threats In Windows Linux And Mac Memory|914|6.3 MB|491|
|7306|The Art Of SQL Server Filestream A Quick Start Guide For Developers And Administrators|487|6.2 MB|57|
|7308|The Art Of XSD SQL Server XML Schema Collections|492|9.7 MB|72|
|7310|The Best Of SQL Servercentral Vol 7|350|6.6 MB|51|
|7312|The C++ Standard Library Second Edition|1190|6.6 MB|340|
|7314|The Definitive Guide To Django Web Development Second Edition|538|5.5 MB|111|
|7316|The Definitive Guide To Jython|545|6.4 MB|68|
|7318|The Definitive Guide To Suse Linux Enterprise Server 12|546|12.0 MB|436|
|7320|The Graphic Designers And Illustr|109|6.9 MB|49|
|7322|The Linux Command Line|482|5.0 MB|845|
|7324|The Linux Programming Interface|1556|7.1 MB|535|
|7326|Thinking In C#|957|4.7 MB|513|
|7328|Twisted Network Programming Essentials 2nd Edition|193|5.7 MB|502|
|7330|Understanding Linux Network Internals|1064|6.8 MB|628|
|7332|User-Centered Web Development|178|7.1 MB|78|
|7334|Visual Web Developer 2005 Express Edition For Dummies|372|7.7 MB|83|
|7336|Web Analytics For Dummies|387|7.6 MB|100|
|7338|Web Database Applications With PHP And MySQL|818|6.3 MB|504|
|7340|Web Development With Javaserver Pages Second Edition|797|7.4 MB|49|
|7342|Web Development With Javaserver Pages|582|13.0 MB|47|
|7344|Webinars For Dummies|292|9.2 MB|24|
|7346|Windows 7 For Dummies Quick Reference|226|5.6 MB|52|
|7348|Windows 8 Elearning Kit For Dummies|418|14.6 MB|36|
|7350|Windows Vista Administration The Definitive Guide|801|18.8 MB|20|
|7352|Windows Vista For Dummies|435|8.0 MB|73|
|7354|WordPress For Dummies 6th Edition Book|431|14.1 MB|527|
|7356|Writer Guide Word Processing With Style|468|10.5 MB|52|
|7358|Yahoo Site Builder For Dummies|363|7.2 MB|51|
|7377|Adobe Creative Cloud Design Tools All-in-One For Dummies|1059|32.6 MB|170|
|7381|An Introduction to Object Oriented Programming with Java 5th Edition|1009|8.4 MB|359|
|7383|Apache CXF Web Service Development|336|4.0 MB|242|
|7385|Applied Architecture Patterns on the Microsoft Platform, 2nd Edition|456|5.7 MB|142|
|7387|Arduino by Example|242|7.6 MB|1100|
|7393|Advanced Wireless Communications 4G Cognitive and Cooperative Broadband Technology, 2nd Edition|890|17.4 MB|233|
|7395|AspectJ in Action|513|5.1 MB|153|
|7397|Beginner Guide To HTML|24|74.0 KB|36|
|7401|Beginning Amazon Web Services with Node.js|249|8.0 MB|210|
|7408|Beginning Apache Struts|537|4.2 MB|92|
|7410|Beginning CSS 3rd Edition|466|11.9 MB|107|
|7415|Beginning CSS Web Development|446|7.5 MB|277|
|7417|Beginning CSS3|547|17.5 MB|419|
|7419|Beginning J2ME 3rd Edition|473|3.5 MB|15|
|7423|Beginning Java ME Platform|574|4.2 MB|80|
|7425|Beginning JSF 2 APIs and JBoss Seam|314|3.5 MB|42|
|7427|beginning oracle sql 3rd edition|429|5.7 MB|305|
|7429|Beginning POJOs|425|4.9 MB|35|
|7431|Blender for Animation and Film-Based Production|279|7.2 MB|151|
|7436|Computer Organization and Architecture, 9th Edition|787|4.0 MB|36|
|7438|Computer System Design System-on-Chip|350|4.2 MB|175|
|7440|Core PHP Programming 3rd Edition|811|3.4 MB|258|
|7442|Build an Awesome PC, 2014 Edition|110|4.2 MB|32|
|7444|Build an HTPC - The Geek|26|3.0 MB|19|
|7448|Buying a Computer For Dummies, 2005 Edition|339|3.3 MB|10|
|7450|Creating your MySQL Database|105|3.4 MB|161|
|7452|Cryptographic Hardware and Embedded Systems- CHES 2015|705|23.8 MB|45|
|7456|CSS and Documents|35|943.5 KB|63|
|7458|CSS Cookbook 3rd Edition|896|28.5 MB|245|
|7460|CSS Pocket Reference 4th Edition|250|1.8 MB|298|
|7465|CSS3 for Web Designers|133|2.8 MB|402|
|7467|CSS3 The Missing Manual 3rd Edition|650|15.0 MB|455|
|7469|Cyber Operations|762|17.2 MB|2264|
|7471|Upgrading and Fixing Computers Do-it-Yourself For Dummies|340|6.5 MB|35|
|7473|USB Complete, 3rd Edition|593|4.8 MB|39|
|7475|VHDL for Logic Synthesis, 3rd Edition|466|2.7 MB|20|
|7477|The iPhone Book, 5th Edition|369|16.4 MB|37|
|7479|The TINI Specification and Developer-s Guide|382|1.3 MB|9|
|7481|Tuscany SCA in Action|474|10.6 MB|17|
|7483|SEO Made Easy|90|1.9 MB|115|
|7485|SEO Made Simple Second Edition|72|928.2 KB|165|
|7487|SEO MYTHS 2014|24|2.7 MB|88|
|7489|SEO Sensei On Page SEO|7|696.0 KB|115|
|7491|SEO Tutorial|39|947.7 KB|163|
|7493|The Definitive Guide to MySQL 5 3rd Edition|785|7.0 MB|199|
|7495|The Definitive Guide to symfony|520|8.0 MB|59|
|7497|Stripes - Java Web Developer|391|3.5 MB|122|
|7499|Supporting Windows 8, 2nd Edition|160|43.6 MB|35|
|7501|Tapestry in Action|585|7.1 MB|17|
|7506|Objective C Fundamentals|368|11.2 MB|14|
|7508|Objective C Phrasebook 2nd Edition Book|348|3.4 MB|29|
|7510|Objective C Programmers Reference Book|375|5.2 MB|35|
|7515|Programming Language Processors in Java- Compilers and Interpreters|438|27.2 MB|231|
|7517|Raspberry Pi A Quick-Start Guide|120|2.5 MB|461|
|7519|Raspberry Pi for Beginners, 2nd Edition|180|28.2 MB|1648|
|7525|Business Management Handbook - Business Degree|84|1.0 MB|57|
|7527|Business Mnagement Careers Guide - Business Degree|12|1.2 MB|37|
|7529|Introduction to Business and Management - Business Degree|6|130.5 KB|34|
|7531|Introduction to Business and Management MN1107 996D107 2790107 - Business Degree|72|354.9 KB|71|
|7533|Introduction to Business Third Edition 2011 - Business Degree|217|3.2 MB|59|
|7535|Object Oriented Programmingin Cpp 4th Edition|1038|8.5 MB|108|
|7537|Objective  C Succinctly|111|1.5 MB|45|
|7539|Objective C for Absolute Beginners 2nd Edition|334|8.8 MB|39|
|7541|Principles of Business Management - Business Degree|13|343.1 KB|46|
|7545|Professional Studies in Business and Management - Business Degree|36|5.5 MB|58|
|7549|Learning SEO from the Experts|31|1.7 MB|123|
|7552|Java Performance Tuning|318|3.4 MB|180|
|7560|MySQL Cookbook 2nd Edition|990|3.4 MB|159|
|7562|MySQL Management and Administration with Navicat|134|4.0 MB|75|
|7564|PHP and script.aculo.us Web 2.0 Application Interfaces|263|4.1 MB|73|
|7566|PHP for Absolute Beginners 2nd Edition|236|3.6 MB|428|
|7568|PHP Unit Essentials|314|4.1 MB|137|
|7570|Pro Android Games 3rd Edition|395|6.2 MB|641|
|7572|Pro CSS3 Animation|178|4.9 MB|460|
|7574|Pro Java 7 NIO.2|296|4.3 MB|205|
|7576|Pro Java ME Apps|355|2.0 MB|85|
|7578|Pro PHP XML and Web Services|936|3.7 MB|243|
|7580|SEO 101 Book|34|544.3 KB|58|
|7582|SEO Guide to Creating Viral Linkbait and Infographics|37|5.1 MB|114|
|7584|Service Oriented Java Business Integration|433|4.4 MB|151|
|7586|The Java EE 6 Tutorial 4th Edition|588|5.0 MB|100|
|7588|The PHP Anthology Volume 2|412|2.1 MB|124|
|7590|Enterprise Games|215|5.2 MB|113|
|7592|Game Development with Unity, 2nd Edition|465|6.2 MB|623|
|7594|Google BigQuery Analytics|530|7.8 MB|129|
|7596|Head First Java 2nd Edition|690|39.7 MB|676|
|7598|Head First Python|493|18.6 MB|1358|
|7600|HTML XHTML And CSS All in One for Dummies 2nd edition|1084|18.2 MB|225|
|7602|HTML5 Tutorial|23|727.0 KB|317|
|7604|Java Pocket Guide|193|887.8 KB|83|
|7606|Oracle RMAN Database Duplication|183|5.4 MB|114|
|7608|PHP Solutions 3rd Edition|499|9.9 MB|236|
|7610|The Ultimate CSS Reference|436|2.9 MB|174|
|7612|Understanding MySQL Internals|256|1.5 MB|148|
|7614|What s New in CSS3|38|4.4 MB|270|
|7616|Wireless Network Security A Beginners Guide|369|20.4 MB|30|
|7618|CompTIA A+ 220-801 and 220-802 Cert Guide, 3rd Edition|174|1.2 MB|0|
|7620|CSS Quick Syntax Reference|130|1.3 MB|113|
|7622|Effective Java 2nd Edition|369|1.5 MB|1011|
|7626|Expert One on One J2EE Development without EJB|577|2.5 MB|115|
|7628|Extending Symfony2 Web Application Framework|140|1.3 MB|69|
|7630|Getting Started with Laravel 4|128|1.4 MB|30|
|7634|Getting Started with MariaDB|100|1.1 MB|121|
|7636|Google Maps API 2nd Edition|76|1.7 MB|117|
|7638|Google Places Cheat Sheet|15|838.6 KB|63|
|7642|Green IT For Dummiess|99|1.5 MB|14|
|7645|Google SEO Secrets 2006|105|1.1 MB|246|
|7647|Guide to Cisco Routers Configuration- Becoming a Router Geek|84|459.6 KB|26|
|7649|Hibernate in Action|430|2.2 MB|18|
|7651|How the Web Works - Introduction to HTML|24|120.1 KB|60|
|7653|HTML and CSS Tutorial|71|716.8 KB|71|
|7655|HTML Basics|18|226.1 KB|29|
|7657|HTML Beginners Guide|16|123.7 KB|39|
|7659|HTML Introduction|22|448.7 KB|45|
|7661|InnoDB|88|1.0 MB|18|
|7663|Instant PHP Web Scraping|60|1.3 MB|287|
|7665|Instant Simple Botting with PHP|62|771.6 KB|177|
|7667|Java and SOAP|230|2.5 MB|166|
|7669|Java NIO|254|2.7 MB|203|
|7671|Java Open Source Programming|482|2.6 MB|114|
|7673|Java Phrasebook|225|819.3 KB|111|
|7675|Java Servlet Programming|528|2.4 MB|88|
|7677|Java The Good Parts|193|2.7 MB|151|
|7679|Java Web Services|249|2.5 MB|205|
|7681|Java Web Services Up and Running|318|1.6 MB|269|
|7683|JDK 1.4 Tutorial|408|2.8 MB|15|
|7685|JSF 2.0 Cookbook|396|2.4 MB|38|
|7687|JSTL in Action|111|1.7 MB|24|
|7691|Learning JavaScript Design Patterns|199|2.5 MB|300|
|7693|Learning JavaScriptMVC|124|1.8 MB|29|
|7695|Learning SEO From The Experts A Step By Step Guide|21|439.8 KB|289|
|7697|Learning XSLT|30|357.7 KB|35|
|7699|Less Web Development Essentials|202|1.9 MB|108|
|7701|Memory Allocation Problems in Embedded Systems- Optimization Method|189|1.6 MB|30|
|7703|Modular Java|245|1.4 MB|114|
|7705|MySQL Enterprise Solutions|419|1.7 MB|145|
|7707|MySQL Pocket Reference 2nd Edition|134|916.1 KB|234|
|7709|Objective C Quick Syntax Reference Book|116|1.9 MB|10|
|7711|Pragmatic Guide to Sass|126|1.6 MB|22|
|7713|Raspberry Pi Home Automation with Arduino, Second Edition|148|2.1 MB|1249|
|7715|RESTful Java with JAX RS|312|2.6 MB|132|
|7717|Sams Teach Yourself Java 6 in 21 Days 5th Edition|721|3.9 MB|169|
|7719|SEO Book The Basics of Search Engine Optimisation|17|183.6 KB|179|
|7721|Seo Fitness Workbook Your Step-By-Step Guide To Dominating Google With Free Seo Tools|46|465.6 KB|423|
|7723|Storm Real-Time Processing Cookbook|254|2.6 MB|42|
|7725|Values Units and Colors|46|2.3 MB|19|
|7728|Cisco ASA, 2nd Edition|1151|28.1 MB|13|
|7730|expert oracle rac performance diagnostics and tuning|690|14.3 MB|136|
|7732|Expert PHP and MySQL|626|16.0 MB|499|
|7734|Google Plus The Missing Manual|231|16.7 MB|79|
|7736|Head First iPhone Development|550|14.2 MB|50|
|7738|Head First Statistics|717|18.5 MB|513|
|7740|JasperReports 3.6 Development Cookbook|456|18.4 MB|43|
|7742|Java and Flex Integration Bible|555|16.5 MB|80|
|7744|Java EE 6 Development with NetBeans 7|392|15.3 MB|111|
|7746|JavaFX Developers Guide|1150|14.4 MB|91|
|7748|Jenkins The Definitive Guide|406|15.2 MB|83|
|7750|Learning PHP MySQL JavaScript CSS and HTML5 3rd Edition|729|18.7 MB|983|
|7752|Learning PHP, MySQL and JavaScript 4th Edition|806|14.2 MB|380|
|7754|Making Things Talk, Second Edition|496|29.9 MB|21|
|7756|Network Security A Beginners Guide Third Edition|337|14.2 MB|28|
|7758|OSGi and Apache Felix 3.0|322|14.8 MB|80|
|7760|PHP Advanced and Object Oriented Programming 3rd Edition|1295|30.4 MB|1154|
|7762|Robot Building for Beginners Third Edition|472|16.1 MB|50|
|7764|TCPIP Illustrated, Volume 1, 2nd Edition|1059|13.9 MB|37|
|7766|Theory of Fun for Game Design 2nd Edition|299|30.5 MB|709|
|7768|Cocos2d-x Game Development Blueprints|392|4.1 MB|126|
|7770|CSS Text|54|3.7 MB|40|
|7772|Expert MySQL 2nd Edition|627|3.8 MB|396|
|7774|GooglePlus For Dummies Portable Edition|146|3.6 MB|14|
|7776|High Availability MySQL Cookbook|276|3.5 MB|154|
|7778|High Performance MySQL 2nd Edition|710|3.6 MB|176|
|7780|Java 2 Enterprise Edition 1.4 Bible|1011|4.0 MB|109|
|7782|Java For Dummies 5th Edition|435|3.5 MB|221|
|7784|Java Network Programming 3rd Edition|762|3.7 MB|115|
|7786|JavaFX 1.2 Application Development Cookbook|332|3.9 MB|121|
|7788|Learning Node.js|301|4.4 MB|59|
|7790|OSWorkflow - A Guide for Java Developers|209|3.5 MB|90|
|7792|Pro Spring Batch|498|4.3 MB|64|
|7794|Pro Wicket - The Experts Voice In Java Technology|327|3.3 MB|79|
|7796|Professional Java JDK 6 Edition|766|4.2 MB|106|
|7798|Programming Google Glass, 2nd Edition|299|4.5 MB|54|
|7800|Raspberry Pi Gaming, 2nd Edition|140|4.4 MB|522|
|7802|Raspberry Pi, 2nd Edition|169|4.2 MB|1048|
|7804|RFID Handbook, 3rd Edition|480|4.5 MB|30|
|7806|Sparrow iOS Game Framework, Beginners Guide|274|3.7 MB|85|
|7808|Game Coding Complete, Fourth Edition|959|5.0 MB|228|
|7812|J2ME in a Nutshell|526|5.0 MB|14|
|7814|Java And XML 2nd Edition|428|5.2 MB|228|
|7816|Java Cookbook 2nd Edition|864|4.9 MB|159|
|7818|Learn 2D Game Development with Csharp|285|5.0 MB|144|
|7820|Learning Modern 3D Graphics Programming|360|4.7 MB|95|
|7822|Microsoft XNA Game Studio 4.0 Learn Programming Now!|465|4.7 MB|92|
|7824|MongoDB Cookbook|737|4.7 MB|96|
|7826|Multi-Threaded Game Engine Design|593|4.6 MB|157|
|7828|Object Oriented Programming Using Java|216|5.0 MB|188|
|7830|PHP Cookbook 3rd Edition|811|5.1 MB|257|
|7832|Physics for JavaScript Games, Animation, and Simulations|490|5.1 MB|151|
|7834|Pro Grunt.js - Using Grunt with JavaScript|165|4.6 MB|112|
|7836|Sass and Compass in Action|238|4.8 MB|66|
|7838|Spring Dynamic Modules in Action|543|4.6 MB|80|
|7840|Spring Recipes 2nd Edition|1105|4.7 MB|22|
|7842|Corona SDK Mobile Game Development Beginners Guide, 2nd Edition|372|5.5 MB|78|
|7844|Creating E-Learning Games with Unity|246|3.0 MB|311|
|7846|Designing Next Generation Web Projects with CSS3|288|5.6 MB|160|
|7848|Filthy Rich Clients|602|6.3 MB|14|
|7850|FPGA Design- Best Practices for Team-based Reuse|260|5.8 MB|40|
|7852|Google Semantic Search|241|5.6 MB|227|
|7854|HTML5 File system API|72|5.3 MB|341|
|7856|JasperReports 3.5 for Java Developers|367|5.6 MB|181|
|7858|Java 2 Micro Edition|504|5.6 MB|59|
|7860|JavaFX 2.0 Introduction by Example|196|3.1 MB|311|
|7862|JMX in Action|424|3.1 MB|19|
|7864|Learning Objective C 2.0 Book|407|3.0 MB|9|
|7866|Learning pandas|604|6.5 MB|204|
|7868|Learning PHP Design Patterns|362|5.8 MB|418|
|7870|LWUIT 1.1 for Java ME Developers|364|5.9 MB|57|
|7872|Mastering phpMyAdmin 3.3.x for Effective MySQL Management|412|6.3 MB|101|
|7874|Mastering-Leap-Motion|361|6.2 MB|15|
|7876|PHP and MongoDB Web Development|292|4.5 MB|324|
|7878|Physics for Game Developers, 2nd Edition|577|5.6 MB|348|
|7880|PowerShell for SQL Server Essentials|186|5.7 MB|272|
|7882|Pro Zend Framework Techniques|266|2.9 MB|18|
|7884|Sass and Compass for Designers|274|5.5 MB|20|
|7886|Scratch 2.0 Beginner-s Guide, 2nd Edition|296|5.5 MB|15|
|7888|Scratch 2.0 Game Development|330|6.3 MB|148|
|7890|Stripes by Example - Java Guide|127|4.9 MB|113|
|7892|UMTS Radio Network Planning, Optimization and QoS Management|343|5.1 MB|15|
|7894|Unity 4.x Cookbook|386|5.3 MB|244|
|7896|XDoclet in Action|625|5.1 MB|9|
|7898|XNA Game Studio 4.0 Programming|526|6.2 MB|82|
|7900|Zend Framework 2.0 by Example|228|5.4 MB|13|
|7902|Eclipse - Programming Java Applications|336|8.5 MB|341|
|7904|Fundamentals of Digital Logic with VHDL Design, 3rd edition|961|8.8 MB|22|
|7906|Game Design Workshop, 3rd Edition|528|8.9 MB|227|
|7908|Google Advertising Tools 2nd Edition|432|12.4 MB|124|
|7910|Google AdWords For Dummies 2nd Edition|437|11.1 MB|340|
|7912|Google Domination Method|179|7.6 MB|78|
|7914|Google Sites and Chrome for Dummies|460|12.9 MB|169|
|7916|Guide to Computer Network Security, 3rd edition|550|7.0 MB|2228|
|7918|HTML5 for .NET Developers|416|11.4 MB|230|
|7920|HTML5 Foundations|386|11.6 MB|655|
|7922|HTML5 JavaScript and jQuery 24 Hour Trainer|411|9.3 MB|1319|
|7924|HTML5 Media|138|11.2 MB|200|
|7926|Interactive Computer Graphics, 6th Edition|778|9.5 MB|156|
|7928|Java Concepts for Java 5 and 6 5th Edition|1118|10.3 MB|165|
|7930|Java Programming 24 Hour Trainer|506|6.7 MB|349|
|7932|JavaServer Faces in Action|1073|9.9 MB|195|
|7934|Learning Android 2nd Edition|288|11.8 MB|1083|
|7936|Learning Cocoa with Objective C 2nd Edition Book|462|7.1 MB|12|
|7938|Learning Core Audio|329|10.2 MB|75|
|7940|Learning C++ by Creating Games with UE4|342|9.4 MB|965|
|7942|Learning Cython Programming using Python|110|12.4 MB|211|
|7944|Learning iCloud Data Management|433|12.1 MB|21|
|7946|Learning iPhone Game Development with Cocos2d 3.0|434|8.3 MB|113|
|7948|Learning JavaScript|350|6.7 MB|135|
|7950|Learning jQuery  4th Edition|444|6.6 MB|1417|
|7952|Learning LibGDX Game Development, 2nd Edition|478|8.0 MB|469|
|7954|Learning Objective-C by Developing iPhone Games|284|6.6 MB|42|
|7956|Learning PHP MySQL JavaScript and CSS|31|6.7 MB|610|
|7958|Learning ROS for Robotics Programming - Second Edition|458|9.1 MB|133|
|7960|Learning Single-page Web Application Development|214|11.0 MB|246|
|7962|Learning Three.js The JavaScript 3D Library for WebGL|402|12.2 MB|255|
|7964|Learning Web App Development|305|13.7 MB|293|
|7966|Learning XNA 4.0|540|7.2 MB|17|
|7968|Libgdx Cross-platform Game Development Cookbook|913|7.8 MB|142|
|7970|Mastering phpMyAdmin 3.4 for Effective MySQL Management|394|9.0 MB|406|
|7972|Micro, Nanosystems and Systems on Chips|318|8.2 MB|15|
|7974|Mobile - Social Game Design- Monetization Methods and Mechanics 2nd Edition |226|7.2 MB|236|
|7976|Mobility Data- Modeling, Management and Understanding|393|11.3 MB|22|
|7978|MySQL High Availability|624|7.6 MB|59|
|7980|MySQL High Availability 2nd Edition|762|10.0 MB|355|
|7982|NHibernate 3.0 Cookbook|328|2.8 MB|71|
|7984|Object Oriented Programming in Cpp|988|10.3 MB|31|
|7986|Objective C for Absolute Beginners 2nd Edition Book|334|10.3 MB|11|
|7988|Portlets in Action|644|11.6 MB|56|
|7990|Practical DWR 2 Projects|570|8.0 MB|15|
|7992|Practical PHP and MySQL Website Databases|437|11.3 MB|1244|
|7994|Practical RichFaces 2nd Edition|405|7.8 MB|36|
|7996|Pro Spring Integration|658|10.3 MB|94|
|7998|Pro Unity Game Development with Csharp|335|10.1 MB|729|
|8000|Programming Concurrency on the JVM|282|2.8 MB|103|
|8002|Real World Solutions for Developing High Quality PHP Frameworks and Applications|410|6.7 MB|763|
|8004|Real-Time Visual Effects for Game Programming|238|12.3 MB|405|
|8006|Selectors Specificity and the Cascade|85|2.9 MB|35|
|8008|Smart Card Handbook, 4th Edition|1072|12.4 MB|101|
|8010|Spring Persistence with Hibernate|265|2.9 MB|81|
|8012|System Center 2012 R2 Virtual Machine Manager Cookbook - Second Edition|428|12.6 MB|82|
|8014|Systems Architecture, 6 edition|658|11.0 MB|81|
|8016|The Game Maker-s Companion|443|13.2 MB|431|
|8022|Active Directory Domain Services 2008 How-To|512|20.8 MB|25|
|8024|Beginning Windows 10 Do More With Your PC|629|24.0 MB|80|
|8026|Beginning Windows Phone 7 Application Development|602|28.0 MB|29|
|8028|Beginning Xcode Swift Edition|544|20.4 MB|225|
|8030|BizTalk 2013 Recipes 2nd Edition|683|25.8 MB|15|
|8032|Cpp for Engineers and Scientists 4th Edition|850|32.7 MB|27|
|8034|Dreamweaver CS6- Visual QuickStart Guide|600|26.7 MB|181|
|8036|Getting Started with Citrix XenApp 6.5|478|20.7 MB|23|
|8038|Group Policy 3rd Edition|1058|28.1 MB|32|
|8042|HTML5 Games Creating Fun with HTML5 CSS3 and WebGL|458|68.5 MB|394|
|8044|Hyper-V for VMware Administrators|337|23.8 MB|37|
|8046|iPAD All In One For Dummies 5th Edition Book|643|33.3 MB|35|
|8048|iPAD All In One For Dummies 6th Edition Book|547|22.7 MB|69|
|8050|iPhone 4S All In One For Dummies|611|22.1 MB|32|
|8052|iPOD And Itunes For Dummies 10th Edition Book|387|20.5 MB|28|
|8054|Learn to Code with Games|296|19.7 MB|39|
|8056|Linux Server Hacks|241|34.1 MB|573|
|8058|Machine Vision Automated Visual Inspection Theory Practice and Applications|802|22.1 MB|68|
|8060|Macs All In One For Dummies 4th Edition Book|867|34.8 MB|25|
|8062|Mastering Web Development With Microsoft Visual Studio 2005|849|24.5 MB|189|
|8064|Microsoft Office 2011 For Mac All In One For Dummies|844|25.1 MB|42|
|8066|Microsoft System Center 2012 Service Manager Cookbook|474|27.5 MB|142|
|8068|Mobile Radio Networks 2nd Edition|1177|63.3 MB|34|
|8070|Modeling Business Objects With Xml Schema|565|24.1 MB|98|
|8072|Objective C Recipes|452|26.4 MB|14|
|8074|Photoshop Elements 7 All In One For Dummies|675|27.9 MB|84|
|8076|Pro Exchange 2013 SP1 PowerShell Administration|628|23.8 MB|135|
|8078|Pro NuGet 2nd Edition|372|26.0 MB|62|
|8080|Pro Oracle Application Express 4 2nd Edition|726|26.3 MB|33|
|8082|Pro VB 2010 and the .NET 4.0 Platform|1801|22.5 MB|32|
|8084|Professional Microsoft IIS 8|983|20.0 MB|253|
|8086|Professional SharePoint 2013 Administration|844|26.0 MB|34|
|8088|Professional SharePoint 2013 Development|820|20.4 MB|24|
|8090|Professional Windows Phone 7 Application Development|626|34.9 MB|30|
|8092|SAP ERP Financial Accounting and Controlling- Configuration and Use Management|579|30.1 MB|170|
|8096|SharePoint Server 2010 Administration 24 Hour Trainer|364|21.4 MB|14|
|8098|Social Media Design For Dummies|355|25.6 MB|43|
|8100|Software Exorcism  A Handbook for Debugging and Optimizing Legacy Code|368|24.2 MB|101|
|8102|Super Scratch Programming Adventure|162|31.8 MB|145|
|8104|Teach Yourself VISUALLY Windows 10|565|28.8 MB|141|
|8106|Technical Analysis For Dummies 2nd Edition Book|349|27.2 MB|664|
|8108|Test Driven - Practical TDD And Acceptance TDD for Java Developers|585|4.2 MB|246|
|8110|The Game Believes in You How Digital Play Can Make Our Kids Smarter|212|2.0 MB|195|
|8112|The Intel Microprocessors 8th Edition|944|6.2 MB|36|
|8114|The LEGO MINDSTORMS EV3 Idea Book|234|31.9 MB|768|
|8116|Ubuntu Linux Bible|931|28.5 MB|709|
|8118|Visual Studio 2013 and .NET 4.5 Expert Cookbook|308|21.7 MB|167|
|8120|Windows 10 Absolute Beginners Guide|676|30.2 MB|97|
|8122|Windows 10 All in One For Dummies|1154|26.6 MB|165|
|8124|Windows 7 Inside Out Deluxe Edition|1359|34.1 MB|116|
|8126|Windows 7 Plain - Simple|401|25.1 MB|56|
|8128|Windows 7 The Definitive Guide|991|21.4 MB|63|
|8130|Windows 8 Tweaks|410|29.8 MB|46|
|8132|Windows XP All In One Desk Reference For Dummies 2nd Edition Book|815|25.1 MB|29|
|8134|WordPress All In One For Dummies|916|26.5 MB|497|
|8136|20 Recipes for Programming MVC 3|120|3.6 MB|30|
|8139|21st Century C|298|2.9 MB|26|
|8141|A Developers Guide to Data Modeling for SQL Server|299|2.7 MB|66|
|8143|Advanced Network Programming - Principles and Techniques|260|6.2 MB|56|
|8145|An Introduction to Network Programming with Java 3rd Edition|389|3.6 MB|162|
|8147|Apache Camel Developers Cookbook|424|3.9 MB|75|
|8149|Apache MyFaces 1.2 Web Application Development|409|8.0 MB|82|
|8151|Beginning ASP.NET MVC 4|292|7.9 MB|124|
|8153|Beginning Django E-Commerce|398|4.0 MB|50|
|8155|Beginning Hibernate 3rd Edition|223|2.2 MB|112|
|8157|Beginning Java 8 Language Features|690|4.6 MB|415|
|8159|Beginning JSP JSF and Tomcat 2nd Edition|426|7.6 MB|41|
|8161|Beginning Python Visualization 2nd Edition|405|6.6 MB|203|
|8163|Beginning SQL Server 2005 Programming|720|5.6 MB|43|
|8165|Beginning SQL Server Modeling|257|7.8 MB|61|
|8167|Beginning Visual C++ 2005|1226|7.6 MB|0|
|8169|Best of Ruby Quiz|285|2.0 MB|26|
|8171|Build Awesome Command-Line Applications in Ruby|214|3.5 MB|17|
|8173|Build Awesome Command-Line Applications in Ruby 2|212|4.0 MB|46|
|8175|Building a Web 2.0 Portal with ASP.NET 3.5|310|4.9 MB|120|
|8177|Building Modular Cloud Apps with OSGi|209|6.8 MB|73|
|8179|Building Software for Simulation|359|5.3 MB|92|
|8181|Burp Suite Starter|70|2.0 MB|20|
|8183|C# 3.0 Cookbook 3rd Edition|888|4.7 MB|0|
|8185|C++ Application Development with CodeBlocks|128|6.4 MB|0|
|8187|C++ Concurrency in Action|530|3.9 MB|0|
|8189|C++ Multithreading Cookbook|422|3.1 MB|0|
|8191|C++ Pocket Reference|138|801.6 KB|0|
|8193|C++ Quick Syntax Reference|108|2.1 MB|0|
|8195|CherryPy Essentials|270|5.2 MB|14|
|8197|Computer Science Programming Basics in Ruby|188|7.8 MB|30|
|8199|Concurrent Programming on Windows|990|8.8 MB|53|
|8201|Continuous Enterprise Development in Java|256|6.9 MB|151|
|8203|Cost-Based Oracle Fundamentals|537|2.8 MB|149|
|8205|Cryptography in C and C++ 2nd Edition|504|1.8 MB|0|
|8207|Data Structures and Algorithms with JavaScript|246|8.7 MB|326|
|8209|Deploying with JRuby|220|4.2 MB|14|
|8211|Developing Microsoft Media Foundation Applications|385|4.2 MB|114|
|8213|DHTML Utopia Modern Web Design Using JavaScript - DOM|338|2.7 MB|67|
|8215|Django 1.0 Template Development|272|5.8 MB|11|
|8217|Drools JBoss Rules 5.X Developer-s Guide|338|4.0 MB|12|
|8219|EJB 3.1 Cookbook|436|4.3 MB|30|
|8221|Eloquent JavaScript 2nd Edition|478|5.1 MB|404|
|8223|Eloquent Ruby|442|4.5 MB|28|
|8225|Enterprise Integration with Ruby|349|2.6 MB|17|
|8227|Enterprise JavaBeans 3.1 6th Edition|764|3.7 MB|34|
|8229|Everyday Scripting with Ruby|426|2.6 MB|24|
|8231|Expert JavaScript|235|3.9 MB|160|
|8233|Expert Oracle and Java Security|466|5.6 MB|146|
|8235|Expert Oracle Database Architecture 2nd Edition|833|6.0 MB|56|
|8237|Expert Oracle Exadata|579|10.7 MB|40|
|8239|Expert Oracle GoldenGate|347|8.4 MB|116|
|8241|Expert Oracle Practices|593|5.3 MB|82|
|8243|Expert PLSQL Practices|508|6.8 MB|29|
|8245|Expert SQL Server 2008 Development|454|9.1 MB|49|
|8247|Expert Visual C++CLI|343|2.6 MB|0|
|8249|Exploring C++ 11 2nd Edition|617|4.0 MB|0|
|8251|Ext GWT 2.0|320|6.8 MB|13|
|8253|ExtGWT Rich Internet Application Cookbook|366|3.1 MB|19|
|8255|Flask Framework Cookbook|258|2.8 MB|36|
|8257|Data Structures and Algorithms in Java 6th Edition|738|10.1 MB|496|
|8259|Expert Python Programming|372|10.2 MB|512|
|8261|From Java To Ruby|158|1.1 MB|72|
|8263|Functional JavaScript|260|8.5 MB|134|
|8265|FXRuby Creat Lean and Mean GUIs With Ruby|217|2.3 MB|29|
|8267|Getting Started with ASP.NET 4.5 Web Forms|62|2.7 MB|154|
|8269|Getting Started with Oracle Tuxedo|162|4.5 MB|21|
|8271|Hands-On Oracle Application Express Security|110|3.2 MB|38|
|8273|HornetQ Messaging Developer-s Guide|250|3.8 MB|17|
|8275|HTML And CSS The Complete Reference 5th Edition|857|10.1 MB|248|
|8277|HTML and JavaScript BASICS 4th Edition|314|9.8 MB|323|
|8279|HTML5 Developers Cookbook|473|7.7 MB|699|
|8281|HTML5 Media|138|5.7 MB|384|
|8283|Instant Mock Testing with PowerMock|82|2.0 MB|44|
|8285|Instant RSpec Test-Driven Development How-to|68|1.3 MB|16|
|8287|Introducing Spring Framework|331|9.9 MB|144|
|8289|Introduction to Programming Using Java Version 6.0|751|6.0 MB|52|
|8291|IPython Notebook Essentials|190|2.2 MB|36|
|8293|Java 7 for Absolute Beginners|311|3.8 MB|221|
|8295|Java 8 in Action|497|9.7 MB|643|
|8297|Java 8 Lambdas|182|6.6 MB|394|
|8299|Java EE 6 Pocket Guide|210|1.9 MB|102|
|8301|Java EE 7 Development with WildFly|471|9.1 MB|202|
|8303|Java EE 7 with GlassFish 4 Application Server|348|6.5 MB|294|
|8305|Java in a Nutshell 6th Edition|418|7.1 MB|347|
|8307|Java Network Programming 4th Edition|502|8.1 MB|247|
|8309|Java Quick Syntax Reference|80|595.3 KB|251|
|8311|Java Web Services Up and Running 2nd Edition|359|9.3 MB|221|
|8313|JavaFX 8 2nd Edition|409|9.3 MB|23|
|8315|JavaScript - DHTML Cookbook 2nd Edition|606|4.8 MB|80|
|8317|JavaScript for Kids A Playful Introduction to Programming|338|10.2 MB|157|
|8319|JavaScript Security|112|2.5 MB|123|
|8321|JavaScript Succinctly|143|1.1 MB|136|
|8323|JavaScript Testing|272|3.0 MB|88|
|8325|JavaScript The Good Parts|172|1.5 MB|131|
|8327|JBoss AS 7 Development|326|5.2 MB|17|
|8329|JRuby Cookbook|224|2.9 MB|20|
|8331|JS Scope and Closures|98|5.8 MB|20|
|8333|JS this and Object Prototypes|173|2.7 MB|59|
|8335|Jump Start JavaScript|185|2.8 MB|121|
|8337|Jump Start Sinatra|166|3.1 MB|32|
|8339|Just Hibernate|139|5.7 MB|94|
|8341|Just Spring|62|1.9 MB|31|
|8343|Just Spring Data Access|76|2.3 MB|29|
|8345|Kivy Interactive Applications in Python|138|1.6 MB|230|
|8347|Learn Python the Hard Way 3rd Edition|306|3.7 MB|343|
|8349|Learn to Program 2nd Edition|231|1.2 MB|22|
|8351|Learning C# 3.0|694|3.5 MB|0|
|8353|Learning Cython Programming|110|10.5 MB|24|
|8355|Learning IPython for Interactive Computing and Data Visualization|138|1.9 MB|73|
|8357|Learning JavaScript Design Patterns|199|2.1 MB|132|
|8359|Learning Oracle PLSQL|524|2.6 MB|22|
|8361|Learning PrimeFaces Extensions Development|192|7.5 MB|41|
|8363|Learning Python Data Visualization|212|5.6 MB|279|
|8365|Learning Python Design Patterns|100|1.1 MB|231|
|8367|Learning Ruby|257|2.7 MB|26|
|8369|Learning SciPy for Numerical and Scientific Computing|150|3.5 MB|94|
|8371|Learning Vaadin|412|6.3 MB|17|
|8373|Lightweight Django Using Rest, Websockets and Backbone|245|4.4 MB|65|
|8375|LINQ Quickly A practical guide to programming Language Integrated Query with C#|250|5.6 MB|0|
|8377|LINQ to Objects Using C# 4.0|331|1.8 MB|0|
|8379|LINQ Unleashed for C#|545|4.9 MB|1|
|8381|MacRuby The Definitive Guide|244|8.9 MB|18|
|8383|Maintainable JavaScript|240|3.2 MB|134|
|8385|Managing Multimedia and Unstructured Data in the Oracle Database|504|4.2 MB|27|
|8387|Mastering HTML5 Forms|148|1.6 MB|716|
|8389|Mastering JavaScript Design Patterns|290|1.8 MB|277|
|8391|Mastering Windows 8 C++ App Development|304|5.2 MB|0|
|8393|matplotlib Plotting Cookbook|222|9.5 MB|34|
|8395|Metaprogramming Ruby|282|5.7 MB|14|
|8397|Metaprogramming Ruby 2nd Edition|262|6.6 MB|29|
|8399|Microsoft ASP.NET and AJAX|352|3.6 MB|323|
|8401|Mobile ASP.NET MVC 5|264|10.3 MB|162|
|8403|Mobile JavaScript Application Development|168|7.8 MB|191|
|8405|Modern C++ Programming with Test-Driven Development|360|5.4 MB|0|
|8407|Moving from C to C++|655|3.6 MB|0|
|8409|MySQL for Python|440|7.1 MB|257|
|8411|NumPy 1.5 Python based Beginners Guide|234|5.5 MB|285|
|8413|NumPy Beginner-s Guide 2nd Edition|310|4.2 MB|25|
|8415|NumPy Cookbook|226|4.7 MB|41|
|8417|Object-Oriented JavaScript|354|6.1 MB|295|
|8419|OCA Java SE 7 Programmer I Certification Guide|562|6.6 MB|166|
|8421|Optimizing Oracle Performance|339|3.1 MB|42|
|8423|Oracle 11g Streams Implementer-s Guide|352|8.5 MB|33|
|8425|Oracle ADF Enterprise Application Development - Made Simple 2nd Edition|432|9.9 MB|31|
|8427|Oracle Advanced PLSQL Developer Professional Guide|440|3.7 MB|54|
|8429|Oracle APEX Best Practices|296|5.5 MB|51|
|8431|Oracle Application Express for Mobile Web Applications|221|10.6 MB|113|
|8433|Oracle Built-in Packages|841|2.5 MB|27|
|8435|Oracle Business Intelligence The Condensed Guide to Analysis and Reporting|184|5.3 MB|121|
|8439|Oracle Data Guard 11gR2 Administration|404|5.7 MB|78|
|8441|Oracle Database 11g|632|8.9 MB|69|
|8443|Oracle Database 12c Performance Tuning Recipes|621|6.0 MB|116|
|8445|Oracle Database Performance and Scalability|729|8.4 MB|68|
|8447|Oracle Database Transactions and Locking Revealed|179|1.7 MB|78|
|8449|Oracle DBA Checklists Pocket Reference|80|539.8 KB|39|
|8451|Oracle Enterprise Manager 12c Command-Line Interface|176|3.3 MB|77|
|8453|Oracle Essentials 4th Edition|408|3.6 MB|52|
|8455|Oracle Exadata Recipes|667|10.0 MB|44|
|8457|Oracle Fusion Applications Administration Essentials|114|6.7 MB|29|
|8459|Oracle Fusion Middleware Patterns|224|9.0 MB|34|
|8461|Oracle PLSQL Language Pocket Reference 4th Edition|180|873.7 KB|66|
|8463|Oracle PLSQL Recipes|457|4.6 MB|75|
|8465|Oracle RMAN Pocket Reference|114|1.3 MB|28|
|8467|Oracle Service Bus 11g Development Cookbook|522|10.2 MB|271|
|8469|Oracle SOA Suite 11g Developer-s Cookbook|346|8.7 MB|34|
|8471|Oracle SQL Recipes|578|4.0 MB|158|
|8473|Oracle SQL Tuning Pocket Reference|90|1,007.6 KB|53|
|8475|Oracle SQL Tuning with Oracle SQLTXPLAIN|333|10.4 MB|158|
|8477|Oracle Web Services Manager|236|9.7 MB|118|
|8479|Oracle WebLogic Server 12c|144|3.6 MB|75|
|8481|Oracle WebLogic Server 12c Advanced Administration Cookbook|285|3.0 MB|67|
|8483|OSGi in Depth|394|4.6 MB|23|
|8485|OSGi Starter|58|2.4 MB|30|
|8487|PeopleSoft for the Oracle DBA|458|5.2 MB|67|
|8489|Play Framework Cookbook|292|2.6 MB|76|
|8491|Pointers in C|161|2.8 MB|39|
|8493|Practical Object-Oriented Design in Ruby|272|2.0 MB|88|
|8495|Practical Programming|369|7.9 MB|21|
|8497|Practical Programming 2nd Edition|388|9.7 MB|44|
|8499|Pragmatic Guide to JavaScript|141|4.6 MB|113|
|8501|Pragmatic Unit Testing in C# with NUnit 2nd Edition|220|1.5 MB|0|
|8503|PrimeFaces Cookbook|328|5.8 MB|74|
|8505|Principles of Data Structures using C and C++|375|2.4 MB|0|
|8507|Pro ASP.NET 4 CMS|316|8.4 MB|87|
|8509|Pro ASP.NET Web API Security|403|6.0 MB|181|
|8511|Pro Django 2nd Edition|290|3.3 MB|56|
|8513|Pro Full-Text Search in SQL Server 2008|297|4.1 MB|34|
|8515|Pro HTML5 with Visual Studio 2012|409|10.5 MB|534|
|8517|Pro IronPython|298|3.3 MB|19|
|8519|Pro JavaScript Design Patterns|298|2.0 MB|210|
|8521|Pro JavaScript for Web Apps|276|4.7 MB|752|
|8523|Pro JavaScript Techniques|380|5.5 MB|213|
|8525|Pro JPA 2 2nd Edition|497|3.4 MB|116|
|8527|Pro ODP.NET for Oracle Database 11g|473|7.4 MB|67|
|8529|Pro Python System Administration 2nd Edition|411|5.2 MB|327|
|8531|Pro Spring Security|330|5.7 MB|61|
|8533|Pro SQL Database for Windows Azure 2nd Edition|306|9.6 MB|215|
|8535|Pro SQL Server 2008 Policy-Based Management|270|8.4 MB|36|
|8537|Professional ASP.NET 2.0 XML|594|7.2 MB|63|
|8539|Professional ASP.NET Design Patterns|722|10.6 MB|136|
|8541|Professional XMPP Programming with JavaScript and jQuery|484|5.3 MB|245|
|8543|Programming ArcGIS 10.1 with Python Cookbook|304|6.1 MB|121|
|8545|Programming in Python 3 2nd Edition|636|6.5 MB|238|
|8547|Programming JavaScript Applications|253|8.4 MB|296|
|8549|Programming Microsoft ASP.NET MVC|590|5.5 MB|269|
|8551|Programming Razor|118|2.8 MB|59|
|8553|Programming Ruby 1.9 - 2.0 4th Edition|868|10.4 MB|319|
|8555|Programming Ruby 1.9 3rd Edition|936|6.4 MB|16|
|8557|Programming Ruby 2nd Edition|833|5.5 MB|16|
|8559|Python and XML Is An Ideal Language For Manipulating Python XML|357|1.8 MB|284|
|8561|Python Cookbook 2nd Edition|846|4.1 MB|78|
|8563|Python Cookbook 3rd Edition|706|5.4 MB|482|
|8565|Python in a Nutshell 2nd Edition|736|5.0 MB|312|
|8567|Python Pocket Reference 5th Edition|264|5.0 MB|322|
|8569|Python Projects|384|9.9 MB|733|
|8571|Python Text Processing with NLTK 2.0 Cookbook|272|4.4 MB|246|
|8573|Refactoring Ruby Edition|481|3.2 MB|37|
|8575|RESTful Java with JAX-RS 2.0 2nd Edition|392|6.9 MB|293|
|8577|RMAN Recipes for Oracle Database 12c 2nd Edition|786|8.2 MB|235|
|8579|Ruby and MongoDB Web Development|332|3.4 MB|186|
|8581|Ruby Best Practices|330|2.0 MB|33|
|8583|Ruby Cookbook|908|4.8 MB|34|
|8585|Ruby in a Nutshell|202|2.4 MB|79|
|8587|Ruby Pocket Reference|178|3.6 MB|70|
|8589|Ruby Quick Syntax Reference|148|1.3 MB|63|
|8591|Ruby Under a Microscope|362|7.0 MB|168|
|8593|Ruby Wizardry|353|6.8 MB|79|
|8595|Sage Beginners Guide|364|7.1 MB|40|
|8597|Sams Teach Yourself C++ in One Hour a Day 7th Edition|767|3.1 MB|0|
|8601|scikit Learn Cookbook|214|2.9 MB|61|
|8603|Scripting in Java|372|3.6 MB|436|
|8605|Sinatra Up and Running|120|4.4 MB|42|
|8608|Speaking JavaScript|460|10.7 MB|429|
|8610|Spring Integration in Action|367|7.2 MB|191|
|8612|Spring Recipes 3rd Edition|848|10.4 MB|983|
|8614|Spring Roo in Action|406|6.2 MB|81|
|8616|Spring Security 3.1|456|6.3 MB|116|
|8618|SQL Server 2008 Transact-SQL Recipes|873|6.9 MB|75|
|8620|SQL Server 2012 T-SQL Recipes 3rd Edition|794|5.2 MB|200|
|8622|SQL Server DMVs in Action|355|10.6 MB|103|
|8624|TeamCity 7 Continuous Integration Essentials|129|3.2 MB|45|
|8626|Test-Drive ASP.NET MVC|280|2.7 MB|98|
|8628|Test-Driven Development with Python|478|9.8 MB|601|
|8630|Test-Driven JavaScript Development|525|2.4 MB|342|
|8632|The Book of JavaScript 2nd Edition|519|6.2 MB|575|
|8634|The Book of Ruby|404|4.3 MB|106|
|8636|The C++ Standard Library 2nd Edition|1190|6.7 MB|0|
|8638|The dRuby Book|266|3.5 MB|45|
|8640|The Ruby Programming Language|446|4.8 MB|155|
|8642|The Truth About HTML5|269|9.1 MB|1550|
|8644|The Well-Grounded Java Developer|496|9.9 MB|761|
|8646|Think Bayes Bayesian Statistics in Python|209|7.0 MB|419|
|8648|Think Python How to Think Like A Computer Scientist|298|3.3 MB|1035|
|8650|Think Stats 2nd Edition Exploratory Data Analysis|225|8.9 MB|149|
|8652|Toad Pocket Reference for Oracle 2nd Edition|130|1.3 MB|167|
|8654|Two Scoops of Django Best Practices For Django 1.5|307|3.3 MB|80|
|8656|Ultra Fast ASP.NET 4.5 2nd Edition|459|7.1 MB|322|
|8658|Understanding and Using C Pointers|226|7.6 MB|192|
|8660|Using JRuby|347|3.7 MB|43|
|8662|Whats New in SQL Server 2012|238|6.9 MB|71|
|8664|WildFly New Features|142|2.2 MB|71|
|8666|Windows via C C++ 5th Edition|801|6.5 MB|0|
|8668|Building Mobile Applications Using Kendo UI Mobile and ASP.NET Web API|256|4.5 MB|361|
|8670|Getting Started with Storm|105|1.8 MB|107|
|8672|HTML CSS The Good Parts|352|4.8 MB|351|
|8674|Introduction to Tornado|136|5.5 MB|197|
|8676|Java 7 New Features Cookbook|385|2.8 MB|303|
|8678|Just Spring Integration|98|1.7 MB|296|
|8680|Oracle Core|277|2.9 MB|381|
|8682|Sams Teach Yourself HTML and CSS in 24 Hours 8th Edition|456|10.1 MB|895|
|8684|Java 8 Pocket Guide|241|8.0 MB|1279|
