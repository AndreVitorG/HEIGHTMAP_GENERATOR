# HEIGHTMAP_GENERATOR
A heightmap generator using python
The program offers the following options:
* Generate new map
* Read and print existing map (csv)
* Save generated map (csv)
* Example map generated
![Map generated by the script](/images/map.png)

----
----

# ALGORITHM

## `Map.create_matrix(Map)`
***Creating the matrix***
* The matrix is initially created using random numbers from 0 to 300 <br>
![Creating the matrix](/images/fig1.png) <br>
----
## `Map.populate(matrix)`
***Creating new rows in between*** 
* New rows are created to fit new numbers <br>
![Creating new lines in between](/images/fig2.png) <br>
***Filling the rows*** 
* The new rows are filled with numbers that have values in between the number above and the number below <br>
![Filling the lines with numbers that have values between the one above and the one below](/images/fig3.png) <br>
***Filling the matrix horizontally*** 
* The process above is repeated but horizontally
* New columns are created with numbers that have values in between the number to the left and to the right <br>
![Filling the matrix the same way but horizontally, the numbers have values between the number to the right and to the left](/images/fig4.png) <br>
***Repeating the process*** 
* Repeating the vertical and horizontal processes one more time <br>
![repeating the process](/images/fig5.png) <br>
![repeating the process](/images/fig6.png) <br>
![repeating the process](/images/fig7.png) <br>
----
## `Map.process_matrix(matrix)`
***Stylizing the map*** 
* Identified the rows by numbers and the columns by letters and symbols
* Changed every number above 100 to 'XXX' and every number below 100 to ' ' <br>
![Stylizing the map and enumerating the rows and columns](/images/fig8.png) <br>

----
----

# CODE

## Calling the methods to create a map
* `from map import Map` first import the Map class.
* The `populate` method is where the magic happens, it can be called infinetely, but the size of the map increases significantly each time.
* The line below calls the populate method twice just like in the images above.
```python
Map.print_matrix(Map.process_matrix(Map.populate(Map.populate(Map.create_matrix(Map)))))
```
* `Map.create_matrix(Map)` - creates the initial ,matrix using random numbers from 0 to 300, the initial matrix size can be defined inside the code (default: height=10,width=8).
* `Map.populate(matrix)` - main algorithm method, fills the matrix vertically and horizontally.
* `Map.process_matrix(matrix)` - enumerates the rows and columns and stylizes the matrix to look more like a map.
* `Map.print_matrix(matrix)` - prints the 2D array in a readable way.

----
----
