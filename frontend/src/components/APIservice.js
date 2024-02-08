export default class APIservice {
  static async GetArticle() {
    const resp = await fetch(`/get`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include',
    });
    return await resp.json();
  }

  static async UpdateArticle(id, body) {
    const resp = await fetch(`/update/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include',
    });
    return await resp.json();
  }

  static async AddArticle(body) {
    const resp = await fetch(`/add`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include',
    });
    return await resp.json();
  }

  static async DeleteArticle(id, body) {
    const resp = await fetch(`/delete/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include',
    });
    return await resp.json();
  }

  static async UserRegister(body) {
    const resp = await fetch(`/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include',
    });
    return await resp.json();
  }

  static async UserLogin(body) {
    const resp = await fetch(`/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include',
    });
    return await resp.json();
  }

  static async GetCurrentUser() {
    const resp = await fetch(`/@me`, {
      method: 'GET',
      credentials: 'include',
    });
    return await resp.json();
  }

  static async Logout() {
    const resp = await fetch(`/logout`, {
      method: 'POST',
      credentials: 'include',
    });
    return await resp.json();
  }
}
