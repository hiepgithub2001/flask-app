import React, { useEffect, useState } from 'react'
import APIservice from '../APIservice'

function Form(props) {

    const [title, setTitle] = useState('')
    const [body, setBody] = useState('')

    useEffect(() => {
        setTitle(props.article.title || '');
        setBody(props.article.body || '');
    }, [props.article]);

    const updateArticle = () => {
        APIservice.UpdateArticle(props.article.id, {title, body})
        .then(resp => props.editArticle(resp))
        .catch(error => console.log(error))
    }

    const addArticle = () => {
        APIservice.AddArticle({title, body})
        .then(resp => props.editArticle(resp))
        .catch(error => console.log(error))
    }

    return (
        <div>
            {props.article ? (
                <div className='mb-3'>

                    <label htmlFor='title' className='form-label'> Title </label>
                    <input
                        type='text'
                        className='form-control'
                        placeholder='Please Enter Title'
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />

                    <label htmlFor='body' className='form-label'> Description </label>
                    <textarea
                        rows="5"
                        value={body}
                        className='form-control'
                        placeholder='Please Enter Description'
                        onChange={(e) => setBody(e.target.value)}
                    />
                    {props.article.id ? (
                        <button
                            className='btn btn-success mt-3'
                            onClick={updateArticle}
                        > Apply </button>
                    ) : (
                        <button
                            className='btn btn-success mt-3'
                            onClick={addArticle}
                        > Apply </button>
                    )}
                </div>
            ):null}
        </div>
    )
}

export default Form
