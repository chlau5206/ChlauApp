// auth.js
function updateUser(userId) {
    fetch(`/auth/update/${userId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}' // Add your CSRF token here
        },
        body: JSON.stringify({ id: userId }) // Optional data
    }).then(response => {
        if (response.ok) {
            alert("User updated successfully!");
        } else {
            alert("Failed to update user.");
        }
    });
}
function deleteUser(userId) {
    fetch(`/auth/delete/${userId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}' // Add your CSRF token here
            },
            body: JSON.stringify({ id: userId }) // Optional data
        }).then(response => {

                if (response.ok) {
                    alert("User deleted successfully!");
                } else {
                    alert("Failed to delete user.");
                }
        });
}

