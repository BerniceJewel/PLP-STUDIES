<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Lists,Images, Tables & Forms </title>
</head>
<body>
    <h1>HTML LISTS</h1>
    <h3>Ordered List:Numbers,Romans,Letters</h3>
    <ol>
        <li>Software Engineering</li>
        <li>Web Development</li>
        <li>Python</li>
        <li>Database</li>
        <li>StartUp Building</li>
    </ol>

  <ol type = "A">
        <li>Software Engineering</li>
        <li>Web Development</li>
        <li>Python</li>
        <li>Database</li>
        <li>StartUp Building</li>
    </ol>
    <ol type="i" start="5">
            <li>Software Engineering</li>
            <li>Web Development</li>
            <li>Python</li>
            <li>Database</li>
            <li>Startup Building</li>
    </ol>
    <h3>Unordered Lists:Bullets,Other shapes</h3>
    <ul>
        <li>Software Engineering</li>
        <li>Web Development</li>
        <li>Python</li>
        <li>Database</li>
        <li>StartUp Building</li>
    </ul>

  <ul type = "Square">
        <li>Software Engineering</li>
        <li>Web Development</li>
        <li>Python</li>
        <li>Database</li>
        <li>StartUp Building</li>
    </ul>
    
   <h3>Defination Lists</h3>
    <dl>
        <dt>HTML<dt>
        <dd>Hyper Text Markup Language</dd>
        <dt>SQL<dt>
            <dd>Structured Query Language</dd>
    </dl>
    

  <h1>HTML IMAGES</h1>
    <h4> ADD IMAGE With copied link directly or download image and insert it.</h4>
    <img src="https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="Image of a Real Estate Development" width="450" height="350">
    <img src="pixels.jpg"alt="Image of a Real Estate Development" width="450" height="350">

  <h1>HTML TABLES</h1>    
    <table border="5">
        <thead>
            <tr>
                <th>NAME</th>
                <th>EMAIL</th>
                <th>COUNTRY</th>
            </tr>
        </thead>
      <tbody>
            <tr>
                <td>Bernice</td>         
                <td>bernice@plp.com</td> 
                <td>Kenya</td>               
            </tr>
            <tr>
                <td>Jemimah</td>         
                <td>jemimah@plp.com</td> 
                <td> Rwanda</td>               
            </tr>
            <tr>
                <td>Gillian</td>         
                <td>gillian@plp.com</td> 
                <td>South Africa</td>               
            </tr>
        </tbody>

  <tfoot>
            <th> tfoot</th>
            <th>Appears at the end of the table.</th>
        </tfoot>

  </table>
  <h1>HTML FORMS</h1>
    <form action="" method="">
        <label for="Name">Name:</label>
        <input type="text" id="Student_name" name="Student_name" required>
        <br><br>
        <label for="Gender">Gender:</label>
        <input type="radio" id="gender" name="gender" value="female"> Female
        <input type="radio" id="gender" name="gender" value="male"> Male
        <br><br>
        <label for="Hobbies">Hobbies:</label>
        <input type="checkbox" name="hobbies" value="sports"> Sports
        <input type="checkbox" name="hobbies" value="music"> Music
        <input type="checkbox" name="hobbies" value="art"> Art
        <input type="checkbox" name="hobbies" value="travel"> Travel
        <br><br>
        <label for="Country">Country:</label>
        <select name="Country" id="Country">
        <option>--Select Country--</option>
        <option value="Nigeria">Nigeria</option>
        <option value="Kenya">Kenya</option>
        <option value="Namibia">Namibia</option>
        <option value="Uganda">Uganda</option>
        </select>
        <br><br>
        <label for="description">Describe yourself:</label>
        <textarea id="description" name="description"></textarea>
        <br><br>
        <button>Register</button>
        <input type="button" value="Cancel">

   </form>


</body>
  
</html>
