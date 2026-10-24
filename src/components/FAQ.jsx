import { useState } from 'react';
import { Plus } from 'lucide-react';
import { questions } from '../data/content.js';

export default function FAQ() {
  const [expanded, setExpanded] = useState(null);

  return (
    <div className="faq-list">
      {questions.map(({ question, answer }, index) => {
        const isExpanded = expanded === index;
        const answerId = `faq-answer-${index}`;
        return (
          <article className={`faq-item${isExpanded ? ' is-expanded' : ''}`} key={question}>
            <h3>
              <button
                className="faq-question"
                type="button"
                aria-expanded={isExpanded}
                aria-controls={answerId}
                onClick={() => setExpanded(isExpanded ? null : index)}
              >
                <span>{question}</span>
                <Plus size={20} aria-hidden="true" />
              </button>
            </h3>
            <div className="faq-answer" id={answerId} hidden={!isExpanded}>
              <p>{answer}</p>
            </div>
          </article>
        );
      })}
    </div>
  );
}
