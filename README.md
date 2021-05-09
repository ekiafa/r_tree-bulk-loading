# R_tree-bulk-loading
R-tree construction through bulk loading
Assignment in the context of [Complex Data Management](https://www.cs.uoi.gr/course/%CE%B4%CE%B9%CE%B1%CF%87%CE%B5%CE%AF%CF%81%CE%B9%CF%83%CE%B7-%CF%83%CF%8D%CE%BD%CE%B8%CE%B5%CF%84%CF%89%CE%BD-%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD/) course ,MYE041,UoI

<h2>Input files</h2>
<li>coords.txt: point coordinates in <x>,<y> format</li>
<li>offsets.txt: entries in <id>,<startOffset>,<endOffset> format,where id is unique, startOffset and endOffset are limits about lines in the file coords.txt that refer to specific id</li>
<li>Rqueries.txt: rectangles that we have to analyse which rectangle objects include</li>
<li>NNqueries.txt: contains points for finding closest neighbors rectagle objects</li>
 
 
 
 <h2>Code files</h2>
 <li>r_tree.py: R tree conctruction by minimum bounding rectangle.Each node containement is >=8 and <=20,root could have >=2 and <=20</li>
 <p>      </p>
 
 > python3 r_tree.py coords.txt offsets.txt
 
 <li>rangeQueries.py: Searching in R-tree by specific window rectangles for finding included rectangle objects or objects that intersect</li>
 <p>      </p>
 
 > python3 rangeQueries.py Rtree.txt Rqueries.txt
 
 <li>bfs_nn.py : incremental NN search in R-tree for finding closest neighbors of specific points</li>
 <p>      </p>
  
 >python3 bfs_nn.py Rtree.txt NNqueries.txt 10
 
 
 <h3>Language</h3>
 <li>Python</li>
  
 <h3>Licence</h3>
 MIT




