import React, { Component } from "react";

class Initializing extends Component {
    state = {
        count: 0,
        alunos: ["Sussy", "Baka"]
    }

    createList() {
        return (this.state.alunos.map((aluno) => (
            <li key={aluno}>{aluno}</li>
        )))
    }

    increment = () => {
        this.state.count++;
        this.setState({ contador: this.state.count + 1 });
        console.log("picapau");
    }

    decrement = () => {
        this.state.count--;
        this.setState({ contador: this.state.count - 1 })
        if (this.state.count < 0) {
            this.state.count = 0;
        }
    }
    render() {
        let classNumber = "number "
        if (this.state.count === 0) {
            classNumber += "red";
        } else {
            classNumber += "green";
        }
        return (
            <>
                <h1 className="titulo">
                    pica pau
                    <span className={classNumber}>
                        {this.state.count}
                    </span>
                </h1>
                <button onClick={this.increment}>Increase</button>
                <button onClick={this.decrement}>Decrease</button>
                {this.state.alunos.length === 0 && 'Não há alunos'}
                <ul>
                    {this.createList()}
                </ul>
            </>
        );
    }
}

export default Initializing;