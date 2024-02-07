import React from 'react'

function ArticleList(props) {
    return (
        <div>
            {props.articles && props.articles.map(article => {
                return (
                    <div key={article.id}>
                        <h1> {article.title} </h1>
                        <p> {article.body} </p>
                        <p> {article.date} </p>
                        <div className='row'>
                            <div className='col-md-1'>
                                <button
                                    className='btn btn-primary'
                                    onClick={() => props.editArticle(article)}
                                >
                                    Update
                                </button>
                            </div>

                            <div className='col'>
                                <button
                                    className='btn btn-danger'
                                    onClick={() => props.deleteArticle(article)}
                                >
                                    Delete
                                </button>
                            </div>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

export default ArticleList
