document.addEventListener('DOMContentLoaded', function() {

    const usersTable = document.querySelector("#userstable")
    const theads = ['id', 'name', 'username', 'email'];

    const thead = document.createElement('thead')

    const headingTr = document.createElement('tr')

    theads.forEach((thContent) => {
        
        const th = document.createElement('th');
        const textNode = document.createTextNode(thContent);

        th.appendChild(textNode)
        headingTr.appendChild(th)
        
    })

    thead.appendChild(headingTr)
    usersTable.appendChild(thead)

    /**
     * 
     * <th></th>
     */

    



})

/*

<table>
    <thead>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>username</th>
            <th>email</th>
        </tr>
    </thead>
</table>

*/