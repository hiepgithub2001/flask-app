export default class APIservice {
  static async GetArticle() {
    const resp = await fetch(`http://127.0.0.1:5000/get`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include'
    });
    return await resp.json();
  }

  static async UpdateArticle(id, body) {
    const resp = await fetch(`http://127.0.0.1:5000/update/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include'
    });
    return await resp.json();
  }

  static async AddArticle(body) {
    const resp = await fetch(`http://127.0.0.1:5000/add`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include'
    });
    return await resp.json();
  }

  static async DeleteArticle(id, body) {
    const resp = await fetch(`http://127.0.0.1:5000/delete/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include'
    });
    return await resp.json();
  }

  static async UserRegister(body) {
    const resp = await fetch(`http://127.0.0.1:5000/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include'
    });
    return await resp.json();
  }

  static async UserLogin(body) {
    const resp = await fetch(`http://127.0.0.1:5000/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include'
    });
    return await resp.json();
  }

  static async GetCurrentUser() {
    const resp = await fetch(`http://127.0.0.1:5000/@me`, {
      method: 'GET',
      credentials: 'include'
    });
    return await resp.json();
  }

  static async Logout() {
    const resp = await fetch(`http://127.0.0.1:5000/logout`, {
      method: 'POST',
      credentials: 'include'
    });
    return await resp.json();
  }
}
