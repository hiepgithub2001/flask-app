import React from 'react';
import { useState, useEffect } from 'react';
import ArticleList from './ArticleList';
import Form from './Form';
import APIservice from '../APIservice';


function ArticleModal() {
    const [articles, setArticles] = useState([]);
    const [editedArticle, setEditedArticle] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/get', {
            'method': 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json())
            .then(resp => setArticles(resp))
            .catch(error => console.log(error))
    }, []);

    useEffect(() => {
        if (!editedArticle || !editedArticle.id) {
            return;
        }

        let new_articles = articles.map(item => {
            return item.id === editedArticle.id ? editedArticle : item;
        })

        if (!articles.map(item => item.id).includes(editedArticle.id)) {
            new_articles.push(editedArticle);
        }

        setArticles(new_articles);
    }, [editedArticle]);

    const removeArticle = (article) => {
        setArticles(articles.filter(item => item.id !== article.id));
    }

    const editArticle = (article) => {
        setEditedArticle(article);
    }

    const deleteArticle = (article) => {
        APIservice.DeleteArticle(article.id)
            .then(resp => removeArticle(resp))
            .catch(error => console.log(error))
    }

    const openForm = () => {
        setEditedArticle({
            title: '',
            body: ''
        })
    }

    return (
        <div className="App">
            <div className='row'>
                <div className='col'>
                    <h1> Welcome hitran! </h1>
                </div>
                <div className='col'>
                    <button
                        className='btn btn-success'
                        onClick={openForm}
                    >
                        Add Article
                    </button>
                </div>
            </div>
            <ArticleList
                articles={articles}
                editArticle={editArticle}
                deleteArticle={deleteArticle}
            />
            {editedArticle ?
                <Form
                    article={editedArticle}
                    editArticle={editArticle}
                /> : null}
        </div>
    );
}

export default ArticleModal
