import React, {Component} from 'react';


class QuestionnaireSelector extends Component {
    constructor() {
        super();
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            nextQuestionId: null
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleChange(e) {
        this.setState({
            nextQuestionId: e.target.value
        })
    }

    handleSubmit(e) {
        e.preventDefault();
        this.props.setNextQuestionId(this.state.nextQuestionId);
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/questionnaires/")
            .then(res => res.json())
            .then(
                (res) => {
                    if (res.results.length) {
                        this.setState({
                            isLoaded: true,
                            items: res.results,
                            nextQuestionId: res.results[0].id
                        });
                    }
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    render() {
        return (
            <div>
                <form
                    onChange={this.handleChange}
                    onSubmit={this.handleSubmit}
                    className="select-questionnaire-form">
                    <p>Please select the questionnaire: </p><select size="1">
                        {this.state.items.map((item, index) => {
                            return (
                                <option key={index} value={item.start_question_id}>{item.name}</option>
                            )
                        })}
                    </select>
                    <input
                        value="Ok"
                        type="submit"/>
                </form>

            </div>
        )
    }
}

export default QuestionnaireSelector;